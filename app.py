from flask import Flask, redirect, request, jsonify, json, session, render_template
from config.db import app, db
from models.Users import Users, UsersSchema




from api.Users import ruta_user
from api.Rutas import ruta_rutas
from api.Alarmas import ruta_alarmas
from api.Comments import ruta_comments
from api.Puntos_E import ruta_puntos_estrategicos

user_schema = UsersSchema()
users_schema = UsersSchema(many=True)



app.register_blueprint(ruta_user, url_prefix="/api_user")
app.register_blueprint(ruta_rutas, url_prefix="/api_rutas")
app.register_blueprint(ruta_alarmas, url_prefix="/api_alarmas")
app.register_blueprint(ruta_comments, url_prefix="/api_comments")
app.register_blueprint(ruta_puntos_estrategicos, url_prefix="/api_puntos_estrategicos")





@app.route("/")
def home():
    return render_template("index.html")

@app.route("/registro", methods = ["POST"])
def registrar():
    usuario = request.form['usuario']
    email = request.form['email']
    password = request.form['password']


@app.route("/ingreso", methods = ["POST"])
def validacion_login():
    email = request.form['email']
    password = request.form['password']
    user = db.session.query(Users.id_user).filter(Users.email == email, Users.password == password).first()
    session['user'] = user
    if user in session:        
        return redirect('/')
    else:
        return redirect('/login')

    

@app.route("/login")
def login():
    return render_template("inicio.html")

@app.route("/comunidad", methods = ["GET", "POST"])
def comunidad():
    return render_template("comunidad.html")


@app.route("/mapa", methods = ["GET", "POST"])
def mapa():
    return render_template("mapa1.html")


if __name__ == "__main__":
    app.run(port=3000, debug=True)