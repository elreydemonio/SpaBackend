from app import ma


class ClientScheama(ma.Schema):
    class Meta:
        fields = (
            'IdClient', 'Nombre', 'Apellido', 'Identifacion', 'Telefono', 'Celular', 'Correo', 'IdSede', 'Sedes_IdSede', 'Activo')
