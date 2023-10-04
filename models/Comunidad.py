from db import app, db, ma

class Comunidad(db.Model):
    __tablename__ = "tblComunidad"

    id_comunidad = db.Column(db.Integer, primary_key = True)
    fecha_creacion = db.Column(db.Date)
    nickname_c = db.Column(db.String(250))

    def __init__(self, fecha_creacion, nickname_c):
        self.fecha_creacion = fecha_creacion
        self.nickname_c = nickname_c

with app.app_context():
    db.create_all()

class ComunidadSchema(ma.Schema):
    class Meta:
        fields = ('id_comunidad', 'fecha_creacion', 'nickname_c')