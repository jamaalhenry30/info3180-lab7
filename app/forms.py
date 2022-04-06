# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import TextAreaField,FileField
from wtforms.validators import InputRequired,FileRequired,FileAllowed

class UploadForm(FlaskForm):
    description = TextAreaField('Description',validators=[InputRequired()])
    photo = FileField('Photo',validators=[FileRequired(),FileAllowed(['jpg','png','Imaged only!'])])