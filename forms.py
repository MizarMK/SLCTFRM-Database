from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, length, Email, equal_to


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), length(min=4, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), equal_to('password')])
    submit = SubmitField('Create Account!')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),length(min=4, max=15)])
    password = PasswordField('Password', validators=[DataRequired(), length(min=8)])
    remember_pass = BooleanField('Remember Password')
    submit = SubmitField('Login')
