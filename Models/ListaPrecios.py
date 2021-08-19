from app import db


class ListaPrecios(db.Model):
    IdPrecio = db.Column(db.Integer, primary_key=True)
    Precio = db.Column(db.DECIMAL)
    Productos = db.relationship('productos')
    Servicios = db.relationship('servicios')