from flask import Flask, render_template, request, redirect

from flask_app.models.users import User

app=Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')


@app.route('/users')
def users():
    user = User.get_all()
    return render_template("users.html", users=user)


@app.route('/user/new')
def new():
    return render_template("new_user.html")

@app.route('/user/create',methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')


if __name__=="__main__":
    app.run(debug=True)