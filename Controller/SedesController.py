from app import app
from Models.Sedes import Sedes


@app.route('/Sedes', methods=['GET'])
def GetSedes():
    return Sedes.Get_Sedes()
