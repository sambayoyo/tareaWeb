from config.db import app, db, ma

class Puntos_E(db.Model):
    __tablename__ = "tblPuntos_E"

    id_PuntoE = db.Column(db.Integer, primary_key = True)
    id_ruta = db.Column(db.Integer, db.ForeignKey('tblRutas.id_ruta'))
    longitud = db.column(db.String(20))
    latitud = db.column(db.String(20))
    tipo_punto = db.column(db.String)

    def __init__(self, id_ruta, longitud, latitud, tipo_punto):
        self.id_ruta = id_ruta
        self.longitud = longitud
        self.latitud = latitud
        self.tipo_punto = tipo_punto

with app.app_context():
    db.create_all()

class Puntos_ESchema(ma.Schema):
    class Meta:
        fields = ('id_PuntoE', 'id_ruta', 'Longitud', 'Latitud', 'tipo_punto')