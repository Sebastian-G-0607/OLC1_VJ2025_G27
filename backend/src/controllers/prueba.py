from flask import Blueprint, jsonify, request

BlueprintPrueba = Blueprint('prueba', __name__)

#!RUTA: http://localhost:4000/
@BlueprintPrueba.route('/api/get-info', methods=['GET'])
def prueba():
    return jsonify({'response': 'Response from the server'})
