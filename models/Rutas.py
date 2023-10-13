from config.db import app, db, ma

class Rutas(db.Model):
    __tablename__ = "tblRutas"

    id_ruta = db.Column(db.Integer, primary_key = True)
    id_u = db.Column(db.Integer, db.ForeignKey('tblUsers.id_user'))
    dir_inicio = db.Column(db.String(50))
    dir_fin = db.Column(db.String(50))

    def __init__(self, id_u, dir_inicio, dir_fin):
        self.id_u = id_u
        self.dir_inicio = dir_inicio
        self.dir_fin = dir_fin

with app.app_context():
    db.create_all()

class RutasSchema(ma.Schema):
    class Meta:
        fields = ('id_ruta', 'id_u', 'dir_inicio', 'dir_fin')