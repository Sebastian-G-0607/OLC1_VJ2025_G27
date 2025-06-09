from flask import Blueprint, jsonify, request
from backend.src.Interprete.parser import parser
from backend.src.Interprete.simbol.RaizArbol import Arbol
from backend.src.Interprete.visitor_object.visitor_output import Visitor_Output

BlueprintPrueba = Blueprint('prueba', __name__)

#!RUTA: http://localhost:4000/
@BlueprintPrueba.route('/api/get-info', methods=['GET'])
def prueba():
    f = open("./backend/src/Interprete/entrada.txt", "r")
    input = f.read()

    #SE OBTIENE EL AST CREADO POR EL PARSER
    try:
        instrucciones = parser.parse(input)
        ast = Arbol(instrucciones)
    except Exception as e:
        return

    if ast is None: 
        print("Hubo un error al parsear la expresión.")
        return
    
    print("AST generado correctamente.")
    visitor = Visitor_Output(ast)

    #SE IMPRIME EL AST
    for nodo in ast.getInstrucciones():
        nodo.accept(visitor)

    print(ast.getConsola())
    return jsonify({'consola': ast.getConsola()})