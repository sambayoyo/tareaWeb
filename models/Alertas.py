from db import app, db, ma
class Alertas (db.Model):
    __tablename__ = "tblAlertas"

    id_u = db.Column(db.Integer(), db.ForeignKey('tblUsuarios.id'))
    texto = db.Column(db.String(50))
    longitud_alerta = db.Column(db.Integer)
    latitud_alerta = db.Column(db.Integer)
    fecha_hora = db.Column(db.Date)

    def __init__(self, id_u, texto, longitud, latitud, fecha):
        self.id_u = id_u
        self.texto = texto
        self.longitud_alerta = longitud
        self.latitud_alerta = latitud
        self.fecha_hora= fecha

with app.app_context():
    db.create_all()

class AlertasSchema(ma.Schema):
    class Meta:
        fields = ('id_u', 'texto', 'longitud_alerta', 'latitud_alerta', 'fecha_hora')       