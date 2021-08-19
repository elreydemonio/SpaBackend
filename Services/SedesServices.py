from app import ma


class SedesScheama(ma.Schema):
    class Meta:
        fields = (
            'IdSede', 'Nombre', 'Direccion', 'Telefono'
        )
