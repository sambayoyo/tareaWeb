from config.db import db, app, ma

class Comments(db.Model):
    __tablename__ = "tblComments"

    id_comentario = db.Column(db.Integer, primary_key = True)
    id_user = db.Column(db.Integer, db.ForeignKey("tblUsers.id_user"))
    contenido = db.Column(db.Text)
    titulo = db.Column(db.Text)
    fecha_hora = db.Column(db.DateTime)
    

    def __init__(self, id_user, contenido, titulo, fecha_hora):
        self.id_user = id_user
        self.contenido = contenido
        self.titulo= titulo
        self.fecha_hora = fecha_hora

with app.app_context():
    db.create_all()

class CommentsSchema(ma.Schema):
    class Meta:
        fields = ('id_comentario', 'id_user', 'contenido','titulo', 'fecha_hora')