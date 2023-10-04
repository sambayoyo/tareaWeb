from db import db, app, ma

class Ciclovias(db.Model):
    __tablename__ = "tblCiclovias"

    id_cv = db.Column(db.Integer, primary_key = True)
    coordenadas_iniciales = db.Column(db.Integer(1000))
    coordenadas_finales = db.Column(db.Integer(1000))

    def __init__(self, coordenadas_iniciales, coordenadas_finales):
        self.coordenadas_iniciales = coordenadas_iniciales
        self.coordenadas_finales = coordenadas_finales

with app.app_context():
    db.create_all()

class CicloviasSchema(ma.Schema):
    class Meta:
        fields = ('id_cv', 'coordenadas_iniciales', 'coordenadas_finales')