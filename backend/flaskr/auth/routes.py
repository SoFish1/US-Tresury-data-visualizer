from . import auth_bp 
from flask import (render_template,  url_for, request, session, flash, g, redirect, current_app, jsonify)
from itsdangerous import SignatureExpired, URLSafeTimedSerializer
from flaskr.auth.email import send_confirmation_email
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

# @auth_bp.route("confirm_email/<token>")
# def confirm_email(token):
#     try:
#         confirm_serializers=URLSafeTimedSerializer(current_app.secret_key)
#         confirmed_email = confirm_serializers.loads(token, salt="email-confirm", max_age=6000)
#         confirmedaccount= User.query.filter_by(email=confirmed_email).first()
#         confirmedaccount.email_confirmed_at = datetime.utcnow()
#         db.session.commit()
                      
#     except SignatureExpired:
#         return render_template("auth/expired_link.html", title = "Link expired!")
        
#     return render_template("auth/confirmed_account.html", title = "Welcome!")



# @auth_bp.route("/reset_password_demand", methods=('GET', 'POST'))
# def reset_password_demand():
#     form = Get_email()


#     email=form.email  

#     if form.validate_on_submit():
#         user = User.query.filter_by(email=form.email.data).first()
#         if user:
            
            
#             flash(('Check your email for the instructions to reset your password'))    
#             #To send confirmation email token
#             confirm_serializers=URLSafeTimedSerializer(current_app.secret_key)
#             token=confirm_serializers.dumps(user.email,salt="reset-password")
#             send_reset_password_email(user.email,token)


#     return render_template("auth/reset_password_demand.html", form=form, title = "Reset Password")


# @auth_bp.route("/reset_password_confirm/<token>", methods=('GET', 'POST'))
# def reset_password_confirm(token):
#     form=Reset_password()
    
#     if form.validate_on_submit():
#         try:
#             confirm_serializers=URLSafeTimedSerializer(current_app.secret_key)
#             confirmed_email = confirm_serializers.loads(token, salt="reset-password", max_age=6000)
#             confirmedaccount= User.query.filter_by(email=confirmed_email).first()
#             confirmedaccount.set_password(form.new_password.data)
#             db.session.commit()
            

#         except SignatureExpired:
#             return render_template("auth/expired_link.html", title = "Link expired!")

#         return redirect(url_for('auth.login'))
                      
    

#     return render_template("auth/reset_password.html", form=form, title = "Reset Password")





@auth_bp.route("/token", methods=["POST"])
@validate(body=UserLogin)
def login():
    
    email = request.body_params.email
    password = request.body_params.password

    user = User.query.filter_by(email=str(email)).first()
    
    if user is None or not user.check_password(password):
        return BaseMessage(message="Bad username or password"), 401
    
    if user.email_confirmed_at is None :
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
        return BaseMessage(message="Something went wrong, the confirmation email has not been sent"), 555

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

