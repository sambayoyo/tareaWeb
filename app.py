from flask import Flask, render_template, request

app = Flask("/")


from api.Clientes import ruta_cliente
from api.Ruta import  ruta_ruta
from api.Alertas import ruta_alertas
from api.Community import ruta_community


app.register_blueprint(ruta_cliente, url_prefix="/api")
app.register_blueprint(ruta_ruta, url_prefix="/api")
app.register_blueprint(ruta_alertas, url_prefix="/api")
app.register_blueprint(ruta_community, url_prefix="/api")


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