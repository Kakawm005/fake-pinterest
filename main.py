from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return "Fakepinterest - Meu primeiro site no ar"

@app.route("/perfil")
def perfil():
    return "perfil do usuario"

if __name__ == "__main__":
    app.run(debug=True)