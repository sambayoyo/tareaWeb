from db import ma, app, db

class Post(db.Model):
    __tablename__ = "tblPost"

    id_post = db.Column(db.Integer, primary_key = True)
    id_user = db.Column(db.Integer, ForeignKey = "tblUsers.id_user")
    id_comentario = db.Column(db.Integer, ForeignKey = "tblComments.id_comentario")
    titulo = db.Column(db.String)
    contenido = db.Column(db.String)
    fecha_hora = db.Column(db.Date)
    

    def __init__(self, id_user, id_comentario, titulo, contenido, fecha_hora):
        self.id_user = id_user
        self.id_comentario = id_comentario
        self.titulo = titulo
        self.contenido = contenido
        self.fecha_hora = fecha_hora

with app.app_context():
    db.create_all()

class PostSchema(ma.Schema):
    class Meta:
        fields = ('id_post', 'id_user', 'id_comentario', 'titulo', 'contenido', 'fecha_hora')