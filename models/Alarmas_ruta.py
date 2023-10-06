from db import app, db, ma
class Alarmas_ruta (db.Model):
    __tablename__ = "tblAlarmas"

    id_alarma = db.Column(db.Integer, primary_key = True)
    id_ruta = db.Column(db.Integer, db.ForeignKey('tblRutas.id_ruta'))
    tipo = db.Column(db.String)

    def __init__(self, id_ruta, tipo):
        self.id_ruta = id_ruta
        self.tipo = tipo
        
with app.app_context():
    db.create_all()

class Alarmas_rutaSchema(ma.Schema):
    class Meta:
        fields = ('id_alarma', 'id_ruta', 'tipo')