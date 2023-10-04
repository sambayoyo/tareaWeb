from flask import Blueprint, jsonify, request,json
from db import db, app, ma
from models.Ciclovias import Ciclovias, CicloviasSchema

ruta_ciclovias = Blueprint("ruta_ciclovias",__name__)

ciclovia_schema = CicloviasSchema()
ciclovias_schema = CicloviasSchema(many=True)

@ruta_ciclovias.route("/ciclovias", methods=["GET"])
def ciclovias():
    resultall = Ciclovias.query.all()# Select * from Ruta;
    result = ciclovias_schema.dump(resultall)
    return jsonify(result)

@ruta_ciclovias.route("/saveciclovia", methods=["POST"])
def saveciclovia():
    data = request.get_json()
    db.session.add(Ciclovias(**data))
    db.session.commit()
    return ciclovia_schema.jsonify(Ciclovias(**data))

@ruta_ciclovias.route("/updateCiclovia", methods=["PUT"])
def updateciclovia():
    id = request.json['id_cv']
    coordenadas_iniciales = request.json['coordenadas_iniciales']
    coordenadas_finales = request.json['coordenadas_finales']
    nCommunity = Ciclovias.query.get(id) 
    nCommunity.coordenadas_iniciales = coordenadas_iniciales
    nCommunity.coordenadas_finales = coordenadas_finales
    db.session.commit()
    return "Datos Actualizado con exitos."

@ruta_ciclovias.route("/deleteCiclovia/<id>", methods=["GET"])
def deletealerta(id):
    ciclovia = Ciclovias.query.get(id)
    db.session.delete(ciclovia)
    db.session.commit()
    return jsonify(ciclovia_schema.dump(ciclovia))