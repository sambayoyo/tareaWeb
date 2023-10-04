from flask import Blueprint, jsonify, request
from db import db
from models.Puntos_estrategicos import Puntos_estrategicos, Puntos_estrategicosSchema

ruta_Puntos_estrategicos = Blueprint("ruta_Puntos_estrategicos",__name__)


punto_estrategicoschema = Puntos_estrategicosSchema()
puntos_estrategicosschema = Puntos_estrategicosSchema(many=True)

@ruta_Puntos_estrategicos.route("/punto_estrategico", methods=["GET"])
def puntos_estrategicos():
    resultall = Puntos_estrategicos.query.all()
    result = puntos_estrategicosschema.dump(resultall)
    return jsonify(result)

@ruta_Puntos_estrategicos.route("/savepunto", methods=["POST"])
def savepuntos_estrategicos():
    data = request.get_json()
    db.session.add(Puntos_estrategicos(**data))
    db.session.commit()
    return punto_estrategicoschema.jsonify(Puntos_estrategicos(**data))

@ruta_Puntos_estrategicos.route("/updatepunto", methods=["PUT"])
def updatepuntos_estrategicos():
    id_PuntoE = request.json['id_PuntoE']
    npuntos_estrategicos = Puntos_estrategicos.query.get(id_PuntoE)
    npuntos_estrategicos.Longitud = request.json['Longitud']
    npuntos_estrategicos.Latitud = request.json['Latitud']
    npuntos_estrategicos.Tipo_punto = request.json['Tipo_punto']
    npuntos_estrategicos.Fecha_creacion = request.json['fecha_creacion']
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_Puntos_estrategicos.route("/deletepunto/<id>", methods=["GET"])
def deletepuntos_estrategicos(id):
    puntos_estrategicos = Puntos_estrategicos.query.get(id)
    db.session.delete(puntos_estrategicos)
    db.session.commit()
    return jsonify(punto_estrategicoschema.dump(puntos_estrategicos))