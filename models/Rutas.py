from config.db import app, db, ma

class Rutas(db.Model):
    __tablename__ = "tblRutas"

    id_ruta = db.Column(db.Integer, primary_key = True)
    id_u = db.Column(db.Integer, db.ForeignKey('tblUsers.id_user'))
    longitud1 = db.Column(db.String(50))
    latitud1 = db.Column(db.String(50))
    longitud2 = db.Column(db.String(50))
    latitud2 = db.Column(db.String(50))

    def __init__(self, id_u, longitud1, latitud1, longitud2, latitud2):
        self.id_u = id_u
        self.longitud1 = longitud1
        self.latitud1 = latitud1
        self.longitud2 = longitud2
        self.latitud2 = latitud2

with app.app_context():
    db.create_all()

class RutasSchema(ma.Schema):
    class Meta:
        fields = ('id_ruta', 'id_u', 'longitud1', 'latitud1', 'longitud2', 'latitud2')