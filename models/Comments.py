from config.db import db, app, ma

class Comments(db.Model):
    __tablename__ = "tblComments"

    id_comentario = db.Column(db.Integer, primary_key = True)
    id_post = db.Column(db.Integer, db.ForeignKey('tblPost.id_post'))
    contenido = db.Column(db.Text)
    fecha_hora = db.Column(db.DateTime)
    

    def __init__(self, id_post, contenido, fecha_hora):
        self.id_post = id_post
        self.contenido = contenido
        self.fecha_hora = fecha_hora

with app.app_context():
    db.create_all()

class CommentsSchema(ma.Schema):
    class Meta:
        fields = ('id_comentario', 'id_post', 'contenido', 'fecha_hora')