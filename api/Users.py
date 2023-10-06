from flask import Blueprint, jsonify, request,json
from db import db, app, ma
from models.Users import Users, UsersSchema

ruta_user = Blueprint("ruta_user",__name__)

user_schema = UsersSchema()
users_schema = UsersSchema(many=True)

@ruta_user.route("/users", methods=["GET"])
def users():
    resultall = Users.query.all()
    result = UsersSchema.dump(resultall)
    return jsonify(result)

@ruta_user.route("/saveuser", methods=["POST"])
def saveuser():
    data = request.get_json()
    db.session.add(Users(**data))
    db.session.commit()
    return users_schema.jsonify(Users(**data))

@ruta_user.route("/updateuser", methods=["PUT"])
def updateuser():
    id = request.json['id']
    email = request.json['email']
    password = request.json['password']
    fecha_registro = request.json['fecha_registro']
    nusuario = Users.query.get(id) 
    nusuario.email = email
    nusuario.password = password
    nusuario.fecha_registro = fecha_registro
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_user.route("/deleteuser/<id>", methods=["GET"])
def deleteuser(id):
    usuario = Users.query.get(id)
    db.session.delete(usuario)
    db.session.commit()
    return jsonify(user_schema.dump(usuario))
 