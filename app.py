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

'''@app.route("/Registro", methods=["POST"]) #Para enviar o subir un registro def saveusuario():  
try: 
username=request.form['usuario']
password=request.form['contrasena']
nombre=request.form['nombre']
print(username,password,nombre)
new_usuario = usuario.query.filter_by(username=username).first()  
if new_usuario is None and username != '' and password != '' and nombre != '': 
                new_usuarios = usuario(username,password,nombre)
                db.session.add(new_usuarios)         
                db.session.commit()           
                return redirect ('/login')    
                else:        
                return redirect ('/sign')    
                except Exception as e:   
                return f"Hubo un error {str(e)}"'''



@app.route("/registro", methods = ["POST"])
def registrar():
    usuario = request.form['usuario']
    email = request.form['email']
    password = request.form['password']
    password1 = request.form['password1']
    fecha = (2023, 10, 18)
    user = Users.query.filter_by(email=email).first()
    if user is None:
        if password == password1:
            new_usuarios = Users(usuario, email, password, fecha)
            db.session.add(new_usuarios)         
            db.session.commit()
            return redirect ('/')
        else:
            return "Las contraseñas no coinciden"
    else:
        return "Usuario ya existe"

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

@app.route("/cerrar", methods = ["POST"])
def cerrar_sesion():
    session.pop('user', None)
    return redirect('/login')


@app.route("/login")
def login():
    return render_template("inicio.html")

@app.route("/comunidad", methods = ["GET", "POST"])
def comunidad():
    return render_template("comunidad.html")


@app.route("/mapa", methods = ["GET", "POST"])
def mapa():
    return render_template("mapa.html")


if __name__ == "__main__":
    app.run(port=5000, debug=True)