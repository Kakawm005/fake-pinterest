# criar as rotas do nosso site (os links)
from flask import Flask, render_template, url_for
from fakepinterest import app
from flask_login import login_required



@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/profile/<usuario>")
@login_required
def profile(usuario):
    return render_template("profile.html", usuario=usuario)