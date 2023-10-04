from db import app, db, ma

class Puntos_estrategicos(db.Model):
    __tablename__ = "tblptos_Estrategicos"

    id_PuntoE = db.Column(db.Integer, primary_key = True)
    Longitud = db.column(db.Float (1000))
    Latitud = db.column(db.Float (1000))
    Tipo_punto = db.column(db.String (1000))
    fecha_creacion = db.column(db.Date)

    def __init__(self, Longitud, Latitud, Tipo_punto, fecha_creacion):
        self.Longitud = Longitud
        self.Latitud = Latitud
        self.Tipo_punto = Tipo_punto
        self.fecha_creacion = fecha_creacion

with app.app_context():
    db.create_all()

class Puntos_estrategicosSchema(ma.Schema):
    class Meta:
        fields = ('id_PuntoE', 'Longitud', 'Latitud', 'Tipo_punto', 'fecha_creacion')