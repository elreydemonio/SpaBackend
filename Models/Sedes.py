from app import db
from Services.SedesServices import SedesScheama

Sede_Scheama = SedesScheama()
Sedes_Scheama = SedesScheama(many=True)


class Sedes(db.Model):
    IdSede = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(30))
    Direccion = db.Column(db.String(50))
    Telefono = db.Column(db.Integer)

    @staticmethod
    def Get_Sedes():
        all_sedes = Sedes.query.all()
        results = Sedes_Scheama.jsonify(all_sedes)
        return results
