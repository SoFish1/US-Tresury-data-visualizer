import functools

from flask import (
    Blueprint,  g,  request, session, 
)




auth_bp = Blueprint('auth', __name__, url_prefix='/backend/auth')

from . import routes