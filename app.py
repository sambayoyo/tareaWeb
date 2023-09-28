from flask import Flask, render_template

app = Flask("/")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/comunidad")
def comunidad():
    return render_template("comunidad.html")


if __name__ == "__main__":
    app.run()