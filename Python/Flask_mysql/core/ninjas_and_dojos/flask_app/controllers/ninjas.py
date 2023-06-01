from flask_app import app
from flask import render_template, session,request, redirect
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/ninjas',)
def ninja():
    all_dojos=Dojo.show_dojos()
    return render_template("addNinja.html",all_dojos=all_dojos)


@app.route("/add_ninjas",methods=['POST'])
def add_new_ninja():

    data={
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'age':request.form['age'],
        'dojo_id':request.form['dojo_id']
    }
    Ninja.create_ninja(data)
    return redirect('/ninjas')