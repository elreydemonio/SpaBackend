from app import db
from Services.ClientServices import ClientScheama
from flask import jsonify

Client_Scheama = ClientScheama()
Clients_Scheama = ClientScheama(many=True)


class Clientes(db.Model):
    IdClient = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(50))
    Apellido = db.Column(db.String(50))
    Identifacion = db.Column(db.Integer, unique=True)
    Telefono = db.Column(db.Integer)
    Celular = db.Column(db.Integer, unique=True)
    Correo = db.Column(db.String(100), unique=True)
    IdSede = db.Column(db.Integer)
    Sedes_IdSede = db.Column(db.Integer, db.ForeignKey('sedes.IdSede'))
    Activo = db.Column(db.Boolean)

    def __init__(self, Nombre, Apellido, Identifacion, Telefono, Celular, Correo, IdSede, Sedes_IdSede, Activo):
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Identifacion = Identifacion
        self.Telefono = Telefono
        self.Celular = Celular
        self.Correo = Correo
        self.IdSede = IdSede
        self.Sedes_IdSede = Sedes_IdSede
        self.Activo = Activo

    def getIdClient(self):
        return self.IdClient

    def setIdClient(self, IDClient):
        self.IdClient = IDClient

    def getNombre(self):
        return self.Nombre

    def setNombre(self, Nombre):
        self.Nombre = Nombre

    def getApellido(self):
        return self.Apellido

    def setApellido(self, Apellido):
        self.Apellido = Apellido

    def getIdentifacion(self):
        return self.Identifacion

    def setIdentifacion(self, Identifacion):
        self.Identifacion = Identifacion

    def getTelefono(self):
        return self.Telefono

    def setTelefono(self, Telefono):
        self.Telefono = Telefono

    def getCelular(self):
        return self.Celular

    def setCelular(self, Celular):
        self.Celular = Celular

    def getCorreo(self):
        return self.Correo

    def setCorreo(self, Correo):
        self.Correo = Correo

    def getIdSede(self):
        return self.IdSede

    def setIdSede(self, IdSede):
        self.IdSede = IdSede

    def getSedes_IdSede(self):
        return self.Sedes_IdSede

    def setSedes_IdSede(self, Sedes_IdSede):
        self.Sedes_IdSede = Sedes_IdSede

    def getActivo(self):
        return self.Activo

    def setActivo(self, activo):
        self.Activo = activo

    def addClient(self):
        db.session.add(self)
        db.session.commit()
        return ClientScheama.jsonify(self)

    @staticmethod
    def Get_Clients():
        all_clients = Clientes.query.filter(
            Clientes.Activo == 1
        )
        result = Clients_Scheama.jsonify(all_clients)
        return result

    @staticmethod
    def Get_Client(Id):
        client = Clientes.query.get(Id)
        return ClientScheama(client)

    def Update_Client(self, Id):
        client: Clientes = Clientes.query.get(Id)
        client.setNombre(self.getNombre())
        client.setApellido(self.getApellido())
        client.setCorreo(self.getCorreo())
        client.setCelular(self.getCelular())
        client.setIdSede(self.getIdSede())
        client.setSedes_IdSede(self.getSedes_IdSede())
        client.setIdentifacion(self.getIdentifacion())
        client.setTelefono(self.getTelefono())
        db.session.commit()
        return jsonify('Actualizado Exitosamente')

    @staticmethod
    def Update_status(Id):
        client: Clientes = Clientes.query.get(Id)
        if client.getActivo() == 0:
            client.setActivo(1)
        else:
            client.setActivo(0)
