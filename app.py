from flask import Flask, render_template, request

app = Flask("/")


from api.Usuarios import ruta_usuario
from api.Ruta import  ruta_ruta
from api.Alertas import ruta_alertas
from api.Comentarios import ruta_comentarios
from api.Comunidad import ruta_comunidad
from api.Puntos_estrategicos import ruta_Puntos_estrategicos
from api.Ciclovias import ruta_ciclovias



app.register_blueprint(ruta_usuario, url_prefix="/api")
app.register_blueprint(ruta_ruta, url_prefix="/api")
app.register_blueprint(ruta_alertas, url_prefix="/api")
app.register_blueprint(ruta_comunidad, url_prefix="/api")
app.register_blueprint(ruta_comentarios, url_prefix="/api")
app.register_blueprint(ruta_Puntos_estrategicos, url_prefix="/api")
app.register_blueprint(ruta_ciclovias, url_prefix="/api")

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