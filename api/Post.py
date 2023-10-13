from flask import Blueprint, jsonify, request,json
from ..config.db import db, app, ma
from ..models.Post import Post, PostSchema

ruta_post = Blueprint("ruta_post",__name__)

post_schema = PostSchema()
posts_schema = PostSchema(many=True)

@ruta_post.route("/post", methods=["GET"])
def posts(): 
    resultall = Post.query.all()
    result = posts_schema.dump(resultall)
    return jsonify(result)

@ruta_post.route("/savepost", methods=["POST"])
def savepost():
    id_user = request.json['id_user']
    titulo = request.json['titulo']
    contenido = request.json['contenido']
    fecha_hora = request.json['fecha_hora']
    new_post = Post(id_user, titulo, contenido, fecha_hora)
    db.session.add(new_post)
    db.session.commit()
    return "datos guardados"

@ruta_post.route("/updatepost", methods=["PUT"])
def updatepost():
    id = request.json['id_post']
    id_u = request.json['id_user']
    titulo = request.json['titulo']
    contenido = request.json['contenido']
    fecha_hora = request.json['fecha_hora']
    nalertas = Post.query.get(id)
    nalertas.id_u = id_u
    nalertas.titulo = titulo
    nalertas.contenido = contenido
    nalertas.fecha_hora = fecha_hora
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_post.route("/deletepost/<id>", methods=["GET"])
def deletepost(id):
    post = Post.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return jsonify(post_schema.dump(post))