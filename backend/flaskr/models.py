# from flask_login import UserMixin
from .extensions import db
from werkzeug.security import check_password_hash, generate_password_hash




# Define the User data-model
class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')

    # User authentication information. The collation='NOCASE' is required
    # to search case insensitively when USER_IFIND_MODE is 'nocase_collation'.
    email = db.Column(db.String(255, collation='NOCASE'), nullable=False, unique=True)
    email_confirmed_at = db.Column(db.DateTime())
    password_hash = db.Column(db.String(128))


    #Delete user from backoffice page
    def delete_user(self,user_id):
        deleted_user = self.query.filter_by(id=user_id)
        db.session.delete(deleted_user)
        db.session.commit()

    #Generate password hash
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    #Check password hash
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)






