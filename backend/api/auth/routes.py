from . import auth_bp 
from flask import request, current_app, jsonify
from itsdangerous import SignatureExpired, URLSafeTimedSerializer
from api.auth.email import send_confirmation_email
from ..models import User, db
from datetime import datetime
from sqlalchemy import exc
from time import sleep
from flask_jwt_extended  import create_access_token, jwt_required, get_jwt_identity
from ..schemas import UserRegister, BaseToken, BaseMessage, UserLogin
from flask_pydantic import validate


# Base endpoint for testing
@auth_bp.route("/", methods=["GET"])
def root():
    return{"message": "Hello World"}


@auth_bp.route("/token", methods=["POST"])
@validate(body=UserLogin)
def login():
    
    email = request.body_params.email
    password = request.body_params.password

    user = User.query.filter_by(email=str(email)).first()
    
    if user is None or not user.check_password(password):
        return BaseMessage(message="Bad username or password"), 401
    
    elif user.email_confirmed_at is None :
        return BaseMessage(message="The account is not activated"), 401
    
    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token)


@auth_bp.route("/register", methods=["POST"])
@validate(body=UserRegister)
def register():
    
    email=request.body_params.email

    try:
        
        
        user = User(email=str(email))
        user.set_password(request.body_params.password)
        
        db.session.add(user)
        db.session.commit()
            
    except exc.IntegrityError:
        db.session.rollback()
        
        return BaseMessage(message="This email is already used"), 555

    #Send confirmation email token
    confirm_serializers=URLSafeTimedSerializer(current_app.secret_key)
    token=confirm_serializers.dumps(email,salt="email-confirm")
    try:
        send_confirmation_email(email,token)
    
    except:
        return BaseMessage(message="Something went wrong, the confirmation email has not been sent"), 556

    return jsonify(token),200
   





@auth_bp.route("/validate-email-token", methods=["POST"])
@validate(body=BaseToken)
def confirmed_account():
    try:
        token = request.body_params.token
        confirm_serializers=URLSafeTimedSerializer(current_app.secret_key)
        confirmed_email = confirm_serializers.loads(token, salt="email-confirm", max_age=6000)
        confirmedaccount= User.query.filter_by(email=confirmed_email).first()
        confirmedaccount.email_confirmed_at = datetime.utcnow()
        db.session.commit()
                      
    except SignatureExpired:
        return BaseMessage(message="Expired token"), 555
        
    return BaseMessage(message="Account successfully confirmed!"), 200

