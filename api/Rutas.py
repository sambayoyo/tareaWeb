from flask import Blueprint, jsonify, request,json
from db import db, app, ma
from models.Rutas import Rutas, RutasSchema

ruta_rutas = Blueprint("ruta_rutas",__name__)

ruta_schema = RutasSchema()
rutas_schema = RutasSchema(many=True)

@ruta_rutas.route("/rutas", methods=["GET"])
def rutas(): 
    resultall = Rutas.query.all()
    result = rutas_schema.dump(resultall)
    return jsonify(result)

@ruta_rutas.route("/saveruta", methods=["POST"])
def saveruta():
    data = request.get_json()
    db.session.add(Rutas(**data))
    db.session.commit()
    return ruta_schema.jsonify(Rutas(**data))

@ruta_rutas.route("/updateruta", methods=["PUT"])
def updateruta():
    id = request.json['id_post']
    nalertas = Rutas.query.get(id)
    nalertas.dir_inicio = request.json['dir_inicio']
    nalertas.dir_fin = request.json['dir_fin']
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_rutas.route("/deleteruta/<id>", methods=["GET"])
def deleteruta(id):
    ruta = Rutas.query.get(id)
    db.session.delete(ruta)
    db.session.commit()
    return jsonify(ruta_schema.dump(ruta))