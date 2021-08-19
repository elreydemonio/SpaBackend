from app import db


class Productos(db.Model):
    IdProducto = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(50))
    Cantidad = db.Column(db.Integer)
    IdPrecio = db.Column(db.Integer, db.ForeignKey('lista_precios.IdPrecio'))
