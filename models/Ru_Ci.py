from db import db, app, ma

class Ru_Ci(db.Model):
    __tablename__ = "tblRu_Ci"

    id_RuCi = db.Column(db.Integer, primary_key = True)
    id_r = db.Column(db.Integer, db.ForeignKey('tblRutas.id_r'))
    id_cv = db.Column(db.Integer, db.ForeignKey('tblCiclovias.id_cv'))

    def __init__(self, id_r, id_cv):
        self.id_r = id_r
        self.id_cv = id_cv

with app.app_context():
    db.create_all()

class Ru_CiSchema(ma.Schema):
    class Meta:
        fields = ('id_RuCi', 'id_r', 'id_cv')