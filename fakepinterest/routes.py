# criar as rotas do nosso site (os links)
from flask import Flask, render_template, url_for
from fakepinterest import app
from flask_login import login_required
from fakepinterest.forms import FormLogin, FormCadastro



@app.route("/", methods=["GET", "POST"])
def homepage():
    formlogin = FormLogin()
    return render_template("homepage.html", form=formlogin)


@app.route("/Cadastro", methods=["GET", "POST"])
def cadastro():
    formcadastro = FormCadastro()
    render_template("cadastro.html", form=formcadastro)


@app.route("/profile/<usuario>")
@login_required
def profile(usuario):
    return render_template("profile.html", usuario=usuario)