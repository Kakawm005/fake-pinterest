from flask import Flask, render_template, url_for
from fakepinterest import app
# Criar o banco de dados

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/profile/<usuario>")
def profile(usuario):
    return render_template("profile.html", usuario=usuario)