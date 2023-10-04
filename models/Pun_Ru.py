from db import db, app, ma

class Pun_Ru(db.Model):
    __tablename__ = "tblPun_Ru"

    id_PunRu = db.Column(db.Integer, primary_key = True)
    id_r = db.Column(db.Integer, db.ForeignKey('tblRutas.id_r'))
    id_p = db.Column(db.Integer, db.ForeignKey('tblptos_Estrategicos.id_PuntoE'))

    def __init__(self, id_r, id_p):
        self.id_r = id_r
        self.id_p = id_p

with app.app_context():
    db.create_all()

class Pun_RuSchema(ma.Schema):
    class Meta:
        fields = ('id_PunRu', 'id_r', 'id_p')