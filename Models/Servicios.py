from app import db


class Servicios(db.Model):
    IdServicio = db.Column(db.Integer, primary_key=True)
    Descripcion = db.Column(db.String(150))
    Nombre = db.Column(db.String(50))
    IdPrecio = db.Column(db.Integer, db.ForeignKey('lista_precios.IdPrecio'))
