from flask import Blueprint, jsonify, request,json
from config.db import db
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
    id_u = request.json['id_u']
    dir_inicio = request.json['dir_inicio']
    dir_fin = request.json['dir_fin']
    new_ruta = Rutas(id_u, dir_inicio, dir_fin)
    db.session.add(new_ruta)
    db.session.commit()
    return "datos guardados"

@ruta_rutas.route("/updateruta", methods=["PUT"])
def updateruta():
    id = request.json['id_ruta']
    id_u = request.json['id_u']
    dir_inicio = request.json['dir_inicio']
    dir_fin = request.json['dir_fin']
    nalertas = Rutas.query.get(id)
    nalertas.id_u = id_u
    nalertas.dir_inicio = dir_inicio
    nalertas.dir_fin = dir_fin
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_rutas.route("/deleteruta/<id>", methods=["GET"])
def deleteruta(id):
    ruta = Rutas.query.get(id)
    db.session.delete(ruta)
    db.session.commit()
    return jsonify(ruta_schema.dump(ruta))