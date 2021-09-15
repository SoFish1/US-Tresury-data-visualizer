from flask import url_for, render_template, current_app
from flask_mail import Message
from ..extensions import mail
# from .forms import Confirm_account_form
from threading import Thread

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(subject, sender, recipients, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.html = html_body
    
    Thread(target=send_async_email, args=(current_app._get_current_object(), msg)).start()
    
    

def send_confirmation_email(email,token):
    
    link = current_app.config["FRONT_END_URI"] + "/confirmed_account/"+ token
    send_email('[US Financial data] Confirmation account',
               sender="trashmarket123@gmail.com",
               recipients=[email],
               html_body=render_template("email/confirmation_email.html", link=link )
               )

# def send_reset_password_email(email,token):
#     form=Confirm_account_form()
#     link = url_for("auth.reset_password_confirm",token=token, _external=True)
#     send_email('[US Financial data] Reset password',
#                sender="trashmarket123@gmail.com",
#                recipients=[email],
#                html_body=render_template("email/reset_password_email.html", link=link )
#                )