import os
from flask import Flask
from config import Config




def create_app(config_class=Config):
    """ Flask application factory """

    
     # Create Flask app load config.py
    app = Flask(__name__, instance_relative_config=True, static_folder='../build', static_url_path='/' )
    app.config.from_object(config_class)

    @app.route('/')
    def index():
        return app.send_static_file('index.html')

    #Initialize extensions
    from .extensions import mail, db, migrate, jwt
    mail.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    
    


    from flaskr.auth import auth_bp 
    app.register_blueprint(auth_bp)

    from flaskr.main import main_bp 
    app.register_blueprint(main_bp)

    with app.app_context():
        db.create_all()

    return app

