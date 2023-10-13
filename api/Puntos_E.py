from flask import Blueprint, jsonify, request
from config.db import db
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
    id_ruta = request.json['id_ruta']
    longitud = request.json['longitud']
    latitud = request.json['latitud']
    tipo_punto = request.json['tipo_punto']
    new_punto = Puntos_E(id_ruta, longitud, latitud, tipo_punto)
    db.session.add(new_punto)
    db.session.commit()
    return "datos guardados"

@ruta_puntos_estrategicos.route("/updatepunto", methods=["PUT"])
def updatepuntos_estrategicos():
    id_PuntoE = request.json['id_PuntoE']
    id_ruta = request.json['id_ruta']
    longitud = request.json['longitud']
    latitud = request.json['latitud']
    tipo_punto = request.json['tipo_punto']
    npuntos_estrategicos = Puntos_E.query.get(id_PuntoE)
    npuntos_estrategicos.id_ruta = id_ruta
    npuntos_estrategicos.longitud = longitud
    npuntos_estrategicos.latitud = latitud
    npuntos_estrategicos.tipo_punto = tipo_punto
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_puntos_estrategicos.route("/deletepunto/<id>", methods=["GET"])
def deletepuntos_estrategicos(id):
    puntos_estrategicos = Puntos_E.query.get(id)
    db.session.delete(puntos_estrategicos)
    db.session.commit()
    return jsonify(punto_estrategicoschema.dump(puntos_estrategicos))