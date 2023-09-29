from flask import Blueprint, jsonify, request
from db import db
from models.Puntos_estrategicos import Puntos_estrategicos, Puntos_estrategicosSchema

ruta_Puntos_estrategicos = Blueprint("ruta_Puntos_estrategicos",__name__)


punto_estrategicoschema = Puntos_estrategicosSchema()
puntos_estrategicosSchema = Puntos_estrategicosSchema(many=True)

@ruta_Puntos_estrategicos.route("/punto_estrategico", methods=["GET"])
def puntos_estrategicos():
    resultall = Puntos_estrategicos.query.all()
    result = puntos_estrategicosSchema.dump(resultall)
    return jsonify(result)

@ruta_Puntos_estrategicos.route("/savepunto", methods=["POST"])
def savepuntos_estrategicos():
    Descripcion_punto = request.json['descripcion']
    nombre = request.json['nombre']
    longitud = request.json['longitud']
    latitud = request.json['latitud']
    comentario = request.json['comentario']
    tipo = request.json['tipo']
    new_punto_estrategico = Puntos_estrategicos(Descripcion_punto, nombre, longitud, latitud, comentario, tipo)
    db.session.add(new_punto_estrategico)
    db.session.commit()
    return "Datos guardados con exitos"

@ruta_Puntos_estrategicos.route("/updatepunto", methods=["PUT"])
def updatepuntos_estrategicos():
    id_PuntoE = request.json['id']
    npuntos_estrategicos = Puntos_estrategicos.query.get(id_PuntoE)
    npuntos_estrategicos.Descripcion_Punto = request.json['descripcion']
    npuntos_estrategicos.Nombre_Punto = request.json['nombre']
    npuntos_estrategicos.Longitud = request.json['longitud']
    npuntos_estrategicos.Latitud = request.json['latitud']
    npuntos_estrategicos.Comentarios = request.json['comentario']
    npuntos_estrategicos.Tipo_punto = request.json['tipo']
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_Puntos_estrategicos.route("/deletepunto/<id>", methods=["GET"])
def deletepuntos_estrategicos(id):
    Puntos_estrategicos = Puntos_estrategicos.query.get(id)
    db.session.delete(Puntos_estrategicos)
    db.session.commit()
    return jsonify(punto_estrategicoschema.dump(Puntos_estrategicos))