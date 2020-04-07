from flaskblog import mail
from flask import url_for, current_app
from flask_mail import Message
import secrets
import os
from PIL import Image

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ending = os.path.splitext(form_picture.filename)
    picture_filename = f"{random_hex}{f_ending}"
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_filename)
    
    # Resize the image
    output_size = (125, 125)
    image = Image.open(form_picture)
    image.thumbnail(output_size)

    # Resize the image
    image.save(picture_path)

    # Return the file_name
    return picture_filename

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message("Password Reset Request", sender='noreply@demo.com', recipients=[user.email])
    msg.body =f"""To reset your password, visit the following link:\n {url_for('reset_token', token=token, _external=True)}\nIf you did not request this email simply ignore this email and no changes will occur."""
    mail.send(msg)