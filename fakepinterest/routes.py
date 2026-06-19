# criar as rotas do nosso site (os links)
from flask import Flask, render_template, url_for, redirect
from flask_login import login_required, login_user, logout_user, current_user
from fakepinterest import app, database, bcrypt
from fakepinterest.forms import FormLogin, FormCadastro
from fakepinterest.models import Usuario, Foto


@app.route("/", methods=["GET"])
def homepage():
    return render_template("homepage.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    formlogin = FormLogin()
    if formlogin.validate_on_submit():
        usuario = Usuario.query.filter_by(email=formlogin.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, formlogin.senha.data):
            login_user(usuario, remember=True)
            return redirect(url_for("profile", usuario=usuario.username))
    return render_template("login.html", form=formlogin)


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    formcadastro = FormCadastro()
    if formcadastro.validate_on_submit():
        senha = bcrypt.generate_password_hash(formcadastro.senha.data)
        usuario = Usuario(username=formcadastro.username.data, email=formcadastro.email.data, senha=senha)
        database.session.add(usuario)
        database.session.commit()
        login_user(usuario, remember=True)
        return redirect(url_for("profile", usuario=usuario.username))
    return render_template("cadastro.html", form=formcadastro)


@app.route("/profile/<usuario>")
@login_required
def profile(usuario):
    return render_template("profile.html", usuario=usuario)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))