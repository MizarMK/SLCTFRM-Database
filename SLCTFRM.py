from flask import Flask, render_template, url_for, flash, redirect
from forms import RegisterForm, LoginForm
import sys

app = Flask(__name__)
app.config['SECRET_KEY'] = '939a1ee77bf825cf3fb65f05e9b8358c' # key for password encryption

userData = ['Mizar', 'HOU', 2019]

@app.route("/")
def mainpage():
	return render_template('Landing.html', title='Home')

@app.route("/login", methods=['GET', 'POST'])
def loginpage():
	form = LoginForm()
	if form.validate_on_submit():
		if form.username.data == 'Mizar': 	# temporary username check; use database to check creds
			flash(f'Welcome Back, { form.username.data }!', 'success')
			return redirect(url_for('dashboard'))
		else:
			flash('Invalid username or password. Please Re-enter fields', 'danger')
	return render_template('Login.html', title='Login', form=form)

@app.route("/register", methods=['GET', 'POST'])
def registrationpage():
	form = RegisterForm()
	if form.validate_on_submit():
		flash(f'Account Created Successfully! Login Now, { form.username.data }!', 'success')
		return redirect(url_for('loginpage'))
	return render_template('Register.html', title='Register', form=form)

@app.route("/dashboard")
def dashboard():
	return render_template('Dashboard.html', title='Dashboard', userData=userData)

if __name__ == '__main__':
	app.run(debug=True)