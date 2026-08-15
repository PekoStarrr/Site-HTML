from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    nome = request.form.get("name")
    if nome == "admin" and request.form.get("senha") == "1234":
        return redirect(url_for('chat', canal_id=100))
    if nome:
        return redirect(url_for('chat', canal_id=random.randint(10**9, 10**10)))
    return "Erro", 403

@app.route("/channels/@me/<int:canal_id>")
def chat(canal_id):
    return render_template("dashboard.html", id_do_canal=canal_id)

app.run(debug=True)
