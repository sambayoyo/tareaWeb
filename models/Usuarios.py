from db import app, db, ma

class Usuarios(db.Model):
    __tablename__ = "tblUsuarios"

    id = db.Column(db.Integer, primary_key = True)
    id_c = db.Column(db.Integer, db.ForeignKey('tblcomunidad.id_comunidad'))
    email = db.Column(db.String(50), unique = True)
    password = db.Column(db.String(50))
    nickname = db.Column(db.String(50))

    def __init__(self, id_c, email, password, nickname):
        self.id_c = id_c
        self.email = email
        self.password = password
        self.nickname = nickname

with app.app_context():
    db.create_all()

class UsuarioSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_c', 'email', 'password', 'nickname')