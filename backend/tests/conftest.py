from pytest import fixture
from flaskr import create_app
from config import TestingConfig
from flaskr.extensions import db
from flaskr.models import User



@fixture
def testing_app():
    return create_app(config_class=TestingConfig)


@fixture
def client(testing_app):
    yield testing_app.test_client()
    with testing_app.app_context():
        db.drop_all() 

@fixture
def usertable(testing_app):
    with testing_app.app_context():
        yield User


