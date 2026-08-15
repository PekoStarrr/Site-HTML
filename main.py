from flask import Flask, render_template, request, redirect, url_for
import random
import os

app = Flask(__name__)

# Criamos nossa própria contagem de visitas
quantidade_visitas = 0

@app.route("/")
def home():
    global quantidade_visitas
    quantidade_visitas += 1  # Toda vez que alguém abrir a página, soma 1!
    return render_template("login.html", visitas=quantidade_visitas)

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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
