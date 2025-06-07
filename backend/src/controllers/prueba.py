from flask import Blueprint, jsonify, request

BlueprintPrueba = Blueprint('prueba', __name__)

#!RUTA: http://localhost:4000/
@BlueprintPrueba.route('/', methods=['GET'])
def prueba():
    return "Hola"
