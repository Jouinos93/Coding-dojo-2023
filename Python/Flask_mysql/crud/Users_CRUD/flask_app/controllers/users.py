from flask_app import app
from flask import request ,render_template, session, redirect, flash
from flask_app.models.user import User

@app.route('/')
def index():
    return redirect('/users')


@app.route('/users')
def users():
    user = User.get_all()
    return render_template("users.html", user=user)


@app.route('/user/new')
def new():
    return render_template("new_user.html")

@app.route('/user/create',methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')

@app.route('/user/edit/<int:id>')
def edit(id):
    data={"id":id}
    return render_template("edit_user.html",user=User.get_one (data))

