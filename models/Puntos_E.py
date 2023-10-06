from db import app, db, ma

class Puntos_E(db.Model):
    __tablename__ = "tblPuntos_E"

    id_PuntoE = db.Column(db.Integer, primary_key = True)
    longitud = db.column(db.Float)
    latitud = db.column(db.Float)
    tipo_punto = db.column(db.String)

    def __init__(self, longitud, latitud, tipo_punto):
        self.longitud = longitud
        self.latitud = latitud
        self.tipo_punto = tipo_punto

with app.app_context():
    db.create_all()

class Puntos_ESchema(ma.Schema):
    class Meta:
        fields = ('id_PuntoE', 'Longitud', 'Latitud', 'tipo_punto')