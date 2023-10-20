from flask import Flask, redirect, request, jsonify, json, session, render_template
from config.db import app, db
from models.Users import Users, UsersSchema
import datetime

from flask_cors import CORS
CORS(app)
CORS(app, resources={r"/api_comments/*": {"origins": "http://127.0.0.1:5000"}})



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
    if 'usuario' in session:
        logged= True
        return render_template('index.html', usuario=session['usuario'], id_user=session['id_user'], logged=logged)
    else:
        return redirect('/login')




@app.route("/ingreso", methods = ["POST"])
def validacion_login():
    email = request.form['email']
    password = request.form['password']
    user = db.session.query(Users.id_user).filter(Users.email == email, Users.password == password).all()
    id_user = Users.query.filter_by(email=email, password=password).first()
    resultado = users_schema.dump(user)
    if len(resultado)>0:    
        session['id_user'] = id_user.id_user
        session['usuario'] = email
        return redirect('/')
    else:
        return redirect('/login')

@app.route("/cerrar")
def cerrar_sesion():
    session.clear()
    return redirect('/login')


@app.route("/login")
def login():
    return render_template("inicio.html")

@app.route("/comunidad", methods = ["GET", "POST"])
def comunidad():
    return render_template("comunidad.html", id_user=session['id_user'])

@app.route("/mapa", methods = ["GET", "POST"])
def mapa():
    return render_template("mapa.html")

@app.route("/registro", methods=['POST'])
def registrar():
    usuario = request.form['usuario']
    email = request.form['email']
    password = request.form['password']
    password1 = request.form['password1']
    if password==password1:
        fecha_actual = datetime.date.today()
        fecha_formateada = fecha_actual.strftime('%Y-%m-%d')
        new_user = Users(usuario, email, password, fecha_formateada)
        db.session.add(new_user)
        db.session.commit() 
        return redirect("/login")    

    else:
        return ('credenciales invalidas')
    

    

if __name__ == "__main__":
    app.run(port=5000, debug=True)