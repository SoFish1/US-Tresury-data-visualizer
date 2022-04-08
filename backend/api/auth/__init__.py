"""
Blueprint for User Management

Hosts the all user related api as registration, offboarding and login.
"""

from flask import Blueprint

auth_bp = Blueprint('auth', __name__, url_prefix='/backend/auth')

from . import routes 
