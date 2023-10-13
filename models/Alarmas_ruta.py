from config.db import app, db, ma
class Alarmas_ruta (db.Model):
    __tablename__ = "tblAlarmas"

    id_alarma = db.Column(db.Integer, primary_key = True)
    id_r = db.Column(db.Integer, db.ForeignKey('tblRutas.id_ruta'))
    tipo = db.Column(db.String(20))

    def __init__(self, id_r, tipo):
        self.id_r = id_r
        self.tipo = tipo
        
with app.app_context():
    db.create_all()

class Alarmas_rutaSchema(ma.Schema):
    class Meta:
        fields = ('id_alarma', 'id_r', 'tipo')