from flask import Flask, render_template
import sys

app = Flask(__name__)

@app.route("/")
def mainpage():
	return render_template('Landing.html')

@app.route("/login")
def loginpage():
	return render_template('Login.html')

@app.route("/dashboard")
def dashboard():
	return "Let's see some baseball stats here"

if __name__ == '__main__':
	app.run(debug=True)