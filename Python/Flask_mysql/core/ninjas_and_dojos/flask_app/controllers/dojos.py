from flask_app import app
from flask import render_template, session,request, redirect
from flask_app.models.dojo import DojoS
from flask_app.models.ninja import Ninja

@app.route("/")
def root():
    return redirect('/dojo')

@app.route("/create_dojo",methods=["POST"])
def add_dojo():

    Dojo.create_dojo(request.form)
    return redirect("/dojo")

@app.route("/dojo")
def home_page():
    all_dojo=Dojo.show_dojos()
    return render_template("dojospage.html",all_dojo=all_dojo)

@app.route('/dojo/<int:dojo_id>')
def show_dojo(dojo_id):
    data={
        'id':dojo_id
    }
    show=Ninja.show_ninja_in_dojo(data)
    return render_template('show_dojo.html',show=show)
