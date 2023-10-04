from flask import Blueprint, jsonify, request,json
from db import db, app, ma
from models.Usuarios import Usuarios, UsuarioSchema

ruta_usuario = Blueprint("ruta_usuario",__name__)

usuario_schema = UsuarioSchema()
usuario_schema = UsuarioSchema(many=True)

@ruta_usuario.route("/usuarios", methods=["GET"])
def usuarios():
    resultall = Usuarios.query.all()
    result = usuario_schema.dump(resultall)
    return jsonify(result)

@ruta_usuario.route("/saveusuario", methods=["POST"])
def saveusuario():
    data = request.get_json()
    db.session.add(Usuarios(**data))
    db.session.commit()
    return usuario_schema.jsonify(Usuarios(**data))

@ruta_usuario.route("/updateusuario", methods=["PUT"])
def updateusuario():
    id = request.json['id']
    email = request.json['email']
    password = request.json['password']
    nickname = request.json['nickname']
    nusuario = Usuarios.query.get(id) 
    nusuario.email = email
    nusuario.password = password
    nusuario.nickname = nickname
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_usuario.route("/deleteusuario/<id>", methods=["GET"])
def deleteusuario(id):
    usuario = Usuarios.query.get(id)
    db.session.delete(usuario)
    db.session.commit()
    return jsonify(usuario_schema.dump(usuario))
 
 