from .extensions import nav
from flask_nav.elements import Navbar, View, Link, Subgroup, View, Link, Text, Separator
from flask_login import current_user



@nav.navigation()
def mynavbar():

    if current_user.is_authenticated:

        return Navbar(
            'SP500 Predictor',
            View("Logout" , "auth.logout"),
            )
    
    else:
                return Navbar(
            'SP500 Predictor',
            View("Login" , "auth.login"),
            View("Register" , "auth.register")
            )
