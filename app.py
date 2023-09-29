from flask import Flask, render_template, request

app = Flask("/")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("inicio.html")

@app.route("/comunidad", methods = ["GET", "POST"])
def comunidad():
    return render_template("comunidad.html")

# se supone que aqui va el request de los inputs de comentarios nuevos
@app.route("/nuevoComentario", methods = ["GET", "POST"])
def nuevoComentario():
    return render_template("comunidad.html")


if __name__ == "__main__":
    app.run()