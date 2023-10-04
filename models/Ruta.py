from db import app, db, ma

class Ruta(db.Model):
    __tablename__ = "tblRutas"

    id_r = db.Column(db.Integer(), primary_key = True)
    id_u = db.Column(db.Integer(), db.ForeignKey('tblUsuarios.id'))
    coordenadas_iniciales = db.Column(db.Integer(250))
    coordenadas_finales = db.Column(db.Integer(250))
    fecha_creacion = db.Column(db.Date)
    nombre_ruta = db.Column(db.String())

    def __init__(self, id_u, coordenadas_iniciales, coordenadas_finales, fecha_creacion, nombre_ruta):
        self.id_u = id_u
        self.coordenadas_iniciales = coordenadas_iniciales
        self.coordenadas_finales = coordenadas_finales
        self.fecha_creacion = fecha_creacion
        self.nombre_ruta = nombre_ruta

with app.app_context():
    db.create_all()

class RutaSchema(ma.Schema):
    class Meta:
        fields = ('id_r', 'id_u', 'coordendas_iniciales', 'coordenadas_finales', "fecha_creacion", "nombre_ruta")