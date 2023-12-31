from config.db import app, db, ma

class Users(db.Model):
    __tablename__ = "tblUsers"

    id_user = db.Column(db.Integer, primary_key = True)
    usuario = db.Column(db.String(20))
    email = db.Column(db.String(50), unique = True)
    password = db.Column(db.String(50))
    fecha_registro = db.Column(db.Date)

    def __init__(self,usuario,  email, password, fecha_registro):
        self.usuario = usuario
        self.email = email
        self.password = password
        self.fecha_registro = fecha_registro

with app.app_context():
    db.create_all()

class UsersSchema(ma.Schema):
    class Meta:
        fields = ('id_user', 'usuario', 'email', 'password', 'fecha_registro')