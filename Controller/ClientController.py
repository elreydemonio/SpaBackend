from Models.Client import Clientes
from app import app
from flask import request, jsonify


@app.route('/Client', methods=['POST'])
def Add_Client():
    clientes = Clientes(request.json['Nombre'], request.json['Apellido'],
                        request.json['Identificacion'], request.json['Telefono'],
                        request.json['Celular'], request.json['Correo'],
                        request.json['IdSede'], request.json['IdSede'],
                        request.json['Activo'])
    return jsonify("Agrado correctamente"), 200


@app.route('/Clientes', methods=['GET'])
def GetClientes():
    return Clientes.Get_Clients()


@app.route('/Clientes/<Id>', methods=['GET'])
def GetCliente(Id):
    return Clientes.Get_Client(Id), 200


@app.route('/Clientes/<Id>', methods=['PUT'])
def Update_Cliente(Id):
    clientes = Clientes(request.json['Nombre'], request.json['Apellido'],
                        request.json['Identificacion'], request.json['Telefono'],
                        request.json['Celular'], request.json['Correo'],
                        request.json['IdSede'], request.json['IdSede'],
                        request.json['Activo'])
    return Clientes.Update_Client(clientes, Id), 200


@app.route('/ClienteAcitvo/<Id>', methods=['PUT'])
def Update_Activo(Id):
    Clientes.Update_status(Id)
    return jsonify('Actualizado'), 200
