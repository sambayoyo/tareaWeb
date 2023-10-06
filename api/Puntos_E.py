from flask import Blueprint, jsonify, request
from db import db
from models.Puntos_E import Puntos_E, Puntos_ESchema

ruta_puntos_estrategicos = Blueprint("ruta_puntos_estrategicos",__name__)


punto_estrategicoschema = Puntos_ESchema()
puntos_estrategicosschema = Puntos_ESchema(many=True)

@ruta_puntos_estrategicos.route("/punto_estrategico", methods=["GET"])
def puntos_estrategicos():
    resultall = Puntos_E.query.all()
    result = puntos_estrategicosschema.dump(resultall)
    return jsonify(result)

@ruta_puntos_estrategicos.route("/savepunto", methods=["POST"])
def savepuntos_estrategicos():
    data = request.get_json()
    db.session.add(Puntos_E(**data))
    db.session.commit()
    return punto_estrategicoschema.jsonify(Puntos_E(**data))

@ruta_puntos_estrategicos.route("/updatepunto", methods=["PUT"])
def updatepuntos_estrategicos():
    id_PuntoE = request.json['id_PuntoE']
    npuntos_estrategicos = Puntos_E.query.get(id_PuntoE)
    npuntos_estrategicos.longitud = request.json['longitud']
    npuntos_estrategicos.latitud = request.json['latitud']
    npuntos_estrategicos.tipo_punto = request.json['tipo_punto']
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_puntos_estrategicos.route("/deletepunto/<id>", methods=["GET"])
def deletepuntos_estrategicos(id):
    puntos_estrategicos = Puntos_E.query.get(id)
    db.session.delete(puntos_estrategicos)
    db.session.commit()
    return jsonify(punto_estrategicoschema.dump(puntos_estrategicos))