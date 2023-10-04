from flask import Blueprint, jsonify, request,json
from db import db, app, ma
from models.Alertas import Alertas, AlertasSchema

ruta_alertas = Blueprint("ruta_alertas",__name__)

alerta_schema = AlertasSchema()
alertas_schema = AlertasSchema(many=True)

@ruta_alertas.route("/alertas", methods=["GET"])
def alertas(): 
    resultall = Alertas.query.all()
    result = alertas_schema.dump(resultall)
    return jsonify(result)

@ruta_alertas.route("/savealerta", methods=["POST"])
def savealerta():
    data = request.get_json()
    db.session.add(Alertas(**data))
    db.session.commit()
    return alertas_schema.jsonify(Alertas(**data))

@ruta_alertas.route("/updatealerta", methods=["PUT"])
def updatealerta():
    Fecha_creacion = request.json['fecha_creacion']
    nalertas = Alertas.query.get(Fecha_creacion)
    nalertas.Texto = request.json['texto']
    nalertas.Longitud = request.json['longitud_alerta']
    nalertas.Latitud = request.json['latitud_alerta']
    nalertas.Fecha_creacion = request.json['fecha_creacion']
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_alertas.route("/deletealerta/<id>", methods=["GET"])
def deletealerta(fecha_hora):
    alerta = Alertas.query.get(fecha_hora)
    db.session.delete(alerta)
    db.session.commit()
    return jsonify(alerta_schema.dump(alerta))
 
 