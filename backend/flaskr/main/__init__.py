import functools

from flask import (
    Blueprint,  g,  request, session, 
)




main_bp = Blueprint('main', __name__, url_prefix='/backend/main')

from . import routes