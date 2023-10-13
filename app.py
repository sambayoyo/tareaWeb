from flask import Flask, redirect, request, jsonify, json, session, render_template
from config.db import app, db



from api.Users import ruta_user
from api.Rutas import ruta_rutas
from api.Post import ruta_post
from api.Alarmas import ruta_alarmas
from api.Comments import  ruta_comments
from api.Puntos_E import ruta_puntos_estrategicos




app.register_blueprint(ruta_user, url_prefix="/api")
app.register_blueprint(ruta_rutas, url_prefix="/api")
app.register_blueprint(ruta_post, url_prefix="/api")
app.register_blueprint(ruta_alarmas, url_prefix="/api")
app.register_blueprint(ruta_comments, url_prefix="/api")
app.register_blueprint(ruta_puntos_estrategicos, url_prefix="/api")





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
    app.run(port=3000, debug=True)