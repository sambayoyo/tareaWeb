from flask import Blueprint, jsonify, request,json
from db import db, app, ma
from models.Comunidad import Comunidad, ComunidadSchema

ruta_comunidad = Blueprint("ruta_comunidad",__name__)


comunidad_schema = ComunidadSchema()
comunidads_schema = ComunidadSchema(many=True)

@ruta_comunidad.route("/Comunidad", methods=["GET"])
def comunidad():
    resultall = Comunidad.query.all()# Select * from Ruta;
    result = comunidads_schema.dump(resultall)
    return jsonify(result)


@ruta_comunidad.route("/saveComunidad", methods=["POST"])
def savecomunidad():
    data = request.get_json()
    db.session.add(Comunidad(**data))
    db.session.commit()
    return comunidad_schema.jsonify(Comunidad(**data))


@ruta_comunidad.route("/updateComunidad", methods=["PUT"])
def updatecomunidad():
    id = request.json['id_comunidad']
    fecha_creacion = request.json['fecha_creacion']
    nickname = request.json['nickname']
    nCommunity = Comunidad.query.get(id) 
    nCommunity.fecha_creacion = fecha_creacion
    nCommunity.nickname = nickname
    db.session.commit()
    return "Datos Actualizado con exitos."


@ruta_comunidad.route("/deleteComunidad/<id>", methods=["GET"])
def deletecomunidad(id):
    comunidad = Comunidad.query.get(id)
    db.session.delete(comunidad)
    db.session.commit()
    return jsonify(comunidad_schema.dump(comunidad))




