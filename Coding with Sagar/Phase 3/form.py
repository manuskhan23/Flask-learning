from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Email,Length,DataRequired

class RegistrationForm(FlaskForm):
    username=StringField("Enter Name:",validators=[DataRequired(message="Name should not be empty")])
    email=StringField("Enter Email:",validators=[DataRequired(message="Email should not be empty or invalid"),Email()])
    password=PasswordField("Enter Password",validators=[DataRequired(message="Password should not be empty or less than 6 characters"),Length(min=6)])
    submit=SubmitField("Register")