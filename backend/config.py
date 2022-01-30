from os import urandom, path, environ
from dotenv import load_dotenv
from password_file import my_password, my_email


basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config(object):
    # Flask settings
    SECRET_KEY = b'\x11\xa1\x971r\x9a\x1a\t\\l#6*L\xec\xf3,O\xc3\xa4\x933\xc6\xde'

    # Flask-SQLAlchemy settings
    db_host_name = environ["DB_HOST_NAME"]
    db_name = environ["DB_NAME"]
    db_password = environ["DB_PASSWORD"]
    db_user = environ["DB_USER"]
    db_port = environ["DATABASE_PORT"]

    #SQLALCHEMY_DATABASE_URI = f'postgresql://{db_user}:{db_password}@{db_host_name}:{db_port}/{db_name}'
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL') or \
        'sqlite:///' + path.join(basedir, 'app.db')
    #SQLALCHEMY_TRACK_MODIFICATIONS = False    # Avoids SQLAlchemy warning

    # Flask-Mail SMTP server settings
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_USERNAME = my_email
    MAIL_PASSWORD = my_password
    MAIL_DEFAULT_SENDER = '"MyApp" <noreply@example.com>'
    MAIL_MAX_EMAILS=10


    # Flask-User settings
    USER_APP_NAME = "Flask-User Basic App"      # Shown in and email templates and page footers
    USER_ENABLE_EMAIL = True        # Enable email authentication
    USER_ENABLE_USERNAME = False    # Disable username authentication
    USER_EMAIL_SENDER_NAME = USER_APP_NAME
    USER_EMAIL_SENDER_EMAIL = "noreply@example.com"

    #FRONT END
    FRONT_END_URI = "http://localhost:3000"
    
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL') or \
        'sqlite:///' + path.join(basedir, 'app_test.db')