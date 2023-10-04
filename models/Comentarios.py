from db import db, app, ma

class Comentarios(db.Model):
    __tablename__ = "tblComentarios"

    id_u = db.Column(db.Integer(), db.ForeignKey('tblUsuarios.id'))
    texto = db.Column(db.String(250))
    fecha_hora = db.Column(db.Date)
    

    def __init__(self, id_u, texto, fecha):
        self.id_c = id_u
        self.texto = texto
        self.fecha_hora = fecha

with app.app_context():
    db.create_all()

class ComentariosSchema(ma.Schema):
    class Meta:
        fields = ('id_u', 'texto', 'fecha_hora')