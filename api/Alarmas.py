from flask import Blueprint, jsonify, request,json
from config.db import db
from models.Alarmas_ruta import Alarmas_ruta, Alarmas_rutaSchema

ruta_alarmas = Blueprint("ruta_alarmas",__name__)

alarma_schema = Alarmas_rutaSchema()
alarmas_schema = Alarmas_rutaSchema(many=True)

@ruta_alarmas.route("/alarmas", methods=["GET"])
def alarmas(): 
    resultall = Alarmas_ruta.query.all()
    result = alarmas_schema.dump(resultall)
    return jsonify(result)

@ruta_alarmas.route("/savealarma", methods=["POST"])
def savealarma():
    id_r = request.json['id_r']
    tipo = request.json['tipo']
    new_alarma = Alarmas_ruta(id_r, tipo)
    db.session.add(new_alarma)
    db.session.commit()
    return "datos guardados"

@ruta_alarmas.route("/updatealarma", methods=["PUT"])
def updatealarma():
    id = request.json['id_alarma']
    id_r = request.json['id_r']
    tipo = request.json['tipo']
    nalertas = Alarmas_ruta.query.get(id)
    nalertas.id_r = id_r
    nalertas.tipo = tipo
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_alarmas.route("/deletealarma/<id>", methods=["GET"])
def deletealarma(id):
    alarma = Alarmas_ruta.query.get(id)
    db.session.delete(alarma)
    db.session.commit()
    return jsonify(alarma_schema.dump(alarma))