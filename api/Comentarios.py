from flask import Blueprint, jsonify, request,json
from db import db, app, ma
from models.Comentarios import Comentarios, ComentariosSchema

ruta_comentarios = Blueprint("ruta_comentarios",__name__)

comentario_schema = ComentariosSchema()
comentarios_schema = ComentariosSchema(many=True)

@ruta_comentarios.route("/comentarios", methods=["GET"])
def comentarios(): 
    resultall = Comentarios.query.all()
    result = comentarios_schema.dump(resultall)
    return jsonify(result)

@ruta_comentarios.route("/savecomentario", methods=["POST"])
def savecomentario():
    data = request.get_json()
    db.session.add(Comentarios(**data))
    db.session.commit()
    return comentario_schema.jsonify(Comentarios(**data))

@ruta_comentarios.route("/updatecomentario", methods=["PUT"])
def updatecomentario():
    Fecha_creacion = request.json['fecha_hora']
    nalertas = Comentarios.query.get(Fecha_creacion)
    nalertas.Texto = request.json['texto']
    nalertas.Fecha_creacion = request.json['fecha_creacion']
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_comentarios.route("/deletecomentario/<id>", methods=["GET"])
def deletecomentario(fecha_hora):
    comentario = Comentarios.query.get(fecha_hora)
    db.session.delete(comentario)
    db.session.commit()
    return jsonify(comentario_schema.dump(comentario))