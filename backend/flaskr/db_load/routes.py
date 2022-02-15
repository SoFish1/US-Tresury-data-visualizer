
# from . import db_load_bp 

# @db_load_bp.route("/token", methods=["POST"])
# @validate(body=UserLogin)
# def login():
    
#     email = request.body_params.email
#     password = request.body_params.password

#     user = User.query.filter_by(email=str(email)).first()
    
#     if user is None or not user.check_password(password):
#         return BaseMessage(message="Bad username or password"), 401
    
#     elif user.email_confirmed_at is None :
#         return BaseMessage(message="The account is not activated"), 401
    
#     access_token = create_access_token(identity=email)
#     return jsonify(access_token=access_token)