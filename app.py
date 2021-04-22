#!/usr/local/bin/python3

from flask import Flask, render_template, request
from datetime import datetime

app=Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html', body="Custom body")
    
@app.route('/login',methods=["POST", "GET"])
def login():
	if request.method == "POST":
		user=request.form["email_address"]
		pw=request.form["password"]
		return f"email={user} password={pw}" 
	else:
		return render_template('login.html')

@app.route('/test')
def get_test():
    return 'Test Again'

@app.route('/owner')
def get_owner():
    return 'Hello world from Kara de Leon'

@app.route('/datetime')
def get_datetime():
	# https://www.programiz.com/python-programming/datetime/current-datetime
	now = datetime.now()
	# dd/mm/YY H:M:S
	dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
	return dt_string

@app.route('/bye')
def goodbye():
    return 'Goodbye'

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=5000)
