from flask import Blueprint, jsonify, request,json
from config.db import db
from models.Comments import Comments, CommentsSchema

ruta_comments = Blueprint("ruta_comments",__name__)

comment_schema = CommentsSchema()
comments_schema = CommentsSchema(many=True)

@ruta_comments.route("/comments", methods=["GET"])
def comments(): 
    resultall = Comments.query.all()
    result = comments_schema.dump(resultall)
    return jsonify(result)

@ruta_comments.route("/savecomments", methods=["POST"])
def savecomments():
    id_user = request.json['id_user']
    titulo = request.json['titulo']
    contenido = request.json['contenido']
    fecha_hora = request.json['fecha_hora']
    new_comment = Comments(id_user, contenido, titulo, fecha_hora)
    db.session.add(new_comment)
    db.session.commit()
    return "datos guardados"

@ruta_comments.route("/updatecomments", methods=["PUT"])
def updatecomments():
    id = request.json['id_comentario']
    id_user = request.json['id_user']
    contenido = request.json['contenido']
    fecha_hora = request.json['fecha_hora']
    nalertas = Comments.query.get(id)
    nalertas.id_user = id_user
    nalertas.contenido = contenido
    nalertas.fecha_hora = fecha_hora
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_comments.route("/deletecomments/<id>", methods=["GET"])
def deletecomments(id):
    comentario = Comments.query.get(id)
    db.session.delete(comentario)
    db.session.commit()
    return jsonify(comment_schema.dump(comentario))