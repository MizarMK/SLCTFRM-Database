from flask import render_template, url_for, flash, redirect, request
from SLCTFRM.forms import RegisterForm, LoginForm, UpdateAccountForm
from SLCTFRM import app, _bcrypt, db
from SLCTFRM.models import Account
from flask_login import login_user, logout_user, current_user, login_required

userData = ['Mizar', 'HOU', 2019]


@app.route("/")
def mainpage():
    return render_template('Landing.html', title='Home')


@app.route("/login", methods=['GET', 'POST'])
def loginpage():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        account = Account.query.filter_by(username=form.username.data).first()
        if account and _bcrypt.check_password_hash(account.password, form.password.data):
            login_user(account, remember=form.remember_pass.data)
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password. Please Re-enter fields', 'danger')
    return render_template('Login.html', title='Login', form=form)


@app.route("/register", methods=['GET', 'POST'])
def registrationpage():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f'Account Created Successfully! Login Now, {form.username.data}!', 'success')
        hashPass = _bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        account = Account(username=form.username.data, email=form.email.data, password=hashPass)
        db.session.add(account)
        db.session.commit()
        return redirect(url_for('loginpage'))
    return render_template('Register.html', title='Register', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('mainpage'))


@app.route("/account", methods=['GET', 'POST'])
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        if form.team.data != 'NUL':
            current_user.favTeam = form.team.data
        else:
            current_user.favTeam = None
        db.session.commit()
        flash(f'Account credentials have been changed', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template('Account.html', title='Account', form=form)


@app.route("/dashboard")
@login_required
def dashboard():
    return render_template('Dashboard.html', title='Dashboard', userData=userData)
