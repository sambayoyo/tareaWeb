from flask import Blueprint, jsonify, request,json
from db import db, app, ma
from models.Ruta import Ruta, RutaSchema

ruta_ruta = Blueprint("ruta_ruta",__name__)
#routes_cliente = Blueprint("routes_cliente", __name__)

ruta_schema = RutaSchema()
rutas_schema = RutaSchema(many=True)

@ruta_ruta.route("/rutas", methods=["GET"])
def ruta():
    resultall = Ruta.query.all()# Select * from Ruta;
    result = rutas_schema.dump(resultall)
    return jsonify(result)


@ruta_ruta.route("/saveruta", methods=["POST"])
def saveruta():
    data = request.get_json()
    db.session.add(Ruta(**data))
    db.session.commit()
    return ruta_schema.jsonify(Ruta(**data))

@ruta_ruta.route("/updateruta", methods=["PUT"])
def updateruta():
    id = request.json['id']
    coordenadas_iniciales = request.json['coordenadas_iniciales']
    coordenadas_finales = request.json['coordenadas_finales']
    fecha_creacion = request.json['fecha_creacion']
    nombre_ruta = request.json['nombre_ruta']
    nruta = Ruta.query.get(id) 
    nruta.coordenadas_iniciales = coordenadas_iniciales
    nruta.coordenadas_finales = coordenadas_finales
    nruta.fecha_creacion = fecha_creacion
    nruta.nombre_ruta = nombre_ruta
    db.session.commit()
    return "Datos Actualizado con exitos."


@ruta_ruta.route("/deleteruta/<id>", methods=["GET"])
def deleteruta(id):
    ruta = Ruta.query.get(id)
    db.session.delete(ruta)
    db.session.commit()
    return jsonify(ruta_schema.dump(ruta))






