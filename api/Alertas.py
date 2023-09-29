from flask import Blueprint, jsonify, request,json
from config.db import db, app, ma
from models.Alertas import Alertas, AlertasSchema

ruta_alertas = Blueprint("ruta_alertas",__name__)
#routes_cliente = Blueprint("routes_cliente", __name__)

alerta_schema = AlertasSchema()
alertas_schema = AlertasSchema(many=True)

@ruta_alertas.route("/alertas", methods=["GET"])
def alertas(): 
    resultall = Alertas.query.all()
    result = alertas_schema.dump(resultall)
    return jsonify(result)

@ruta_alertas.route("/savealerta", methods=["POST"])
def savealerta():
    nombre = request.json['nombre']
    new_alerta = Alertas(nombre)
    db.session.add(new_alerta)
    db.session.commit()
    return "Datos guardados con exitos"

@ruta_alertas.route("/updatealerta", methods=["PUT"])
def updatealerta():
    id = request.json['id']
    nombre = request.json['nombre']
    nAlerta = Alertas.query.get(id) #Select * from Cliente where id = id
    nAlerta.nombre = nombre
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_alertas.route("/deletealerta/<id>", methods=["GET"])
def deletecliente(id):
    alerta = Alertas.query.get(id)
    db.session.delete(alerta)
    db.session.commit()
    return jsonify(alerta_schema.dump(alerta))
 
 