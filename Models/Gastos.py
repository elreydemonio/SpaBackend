from app import db


class Gastos(db.Model):
    IdGasto = db.Column(db.Integer, primary_key=True)
    Description = db.Column(db.String(100))
    Gastos = db.Column(db.Integer)
    IdSedeGasto = db.Column(db.Integer, db.ForeignKey('sedes.IdSede'))
