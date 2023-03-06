from flask import render_template, request, redirect

from flask_app import app
from flask_app.models.ninja import Ninja


@app.route('/')
def index():
    return redirect('/ninjas')


@app.route('/ninjas')
def users():
    return render_template("index.html",ninjas=Ninja.get_all())


@app.route('/ninja/new')
def new():
    return render_template("create_new_ninja.html")
