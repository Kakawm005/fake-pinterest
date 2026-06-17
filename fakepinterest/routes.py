# criar as rotas do nosso site (os links)
from flask import Flask, render_template, url_for
from fakepinterest import app, database, bcrypt
from flask_login import login_required
from fakepinterest.forms import FormLogin, FormCadastro
from fakepinterest.models import Usuario, Foto


@app.route("/", methods=["GET", "POST"])
def homepage():
    return render_template("homepage.html")


@app.route("/login")
def login():
    formlogin = FormLogin()
    return render_template("login.html", form=formlogin)


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    formcadastro = FormCadastro()
    if formcadastro.validate_on_submit():
        usuario = Usuario(username=formcadastro.username.data, 
                          email=formcadastro.email.data,
                          senha=formcadastro.senha.data)
    return render_template("cadastro.html", form=formcadastro)


@app.route("/profile/<usuario>")
@login_required
def profile(usuario):
    return render_template("profile.html", usuario=usuario)