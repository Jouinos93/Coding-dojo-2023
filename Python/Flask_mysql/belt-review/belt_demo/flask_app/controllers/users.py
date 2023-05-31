from flask_app import app
from flask import Flask, request,render_template, session, redirect
from flask_app.models.user import User


@app.route('/users')
def index():
    return render_template("index.html")

@app.route('/users/create',methods=['Post'])
def create_user():
    print(request.form)
    if (User.validate(request.form)):
        User.create_user(request.form)
        return redirect ('/dashboard')
    return redirect ('/')

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")