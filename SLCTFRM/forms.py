from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError, SelectField
from wtforms.validators import DataRequired, length, Email, equal_to
from SLCTFRM.models import Account
from flask_login import current_user
import SLCTFRM.dbinit as dbinit

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), length(min=4, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), equal_to('password')])
    submit = SubmitField('Create Account!')

    def validate_username(self, username):
        account = Account.query.filter_by(username=username.data).first()
        if account:
            raise ValidationError('username already in use, please enter a unique one')

    def validate_email(self, email):
        account = Account.query.filter_by(email=email.data).first()
        if account:
            raise ValidationError('email already in use, please enter a unique one')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),length(min=4, max=15)])
    password = PasswordField('Password', validators=[DataRequired(), length(min=8)])
    remember_pass = BooleanField('Remember Password')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), length(min=4, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    team = SelectField(u'Favorite Team', choices=dbinit.teams)
    submit = SubmitField('Confirm Changes')

    def validate_username(self, username):
        if username.data != current_user.username:
            account = Account.query.filter_by(username=username.data).first()
            if account:
                raise ValidationError('username already in use, please enter a unique one')
    def validate_email(self, email):
        if email.data != current_user.email:
            account = Account.query.filter_by(email=email.data).first()
            if account:
                raise ValidationError('email already in use, please enter a unique one')
