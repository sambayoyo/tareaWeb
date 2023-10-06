from flask import Blueprint, jsonify, request,json
from db import db, app, ma
from models.Post import Post, PostSchema

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
    data = request.get_json()
    db.session.add(Post(**data))
    db.session.commit()
    return post_schema.jsonify(Post(**data))

@ruta_post.route("/updatepost", methods=["PUT"])
def updatepost():
    id = request.json['id_post']
    nalertas = Post.query.get(id)
    nalertas.titulo = request.json['titulo']
    nalertas.contenido = request.json['contenido']
    nalertas.fecha_hora = request.json['fecha_hora']
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_post.route("/deletepost/<id>", methods=["GET"])
def deletepost(id):
    post = Post.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return jsonify(post_schema.dump(post))