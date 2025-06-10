from flask import Blueprint, jsonify, request
from backend.src.Interprete.parser import parser
from backend.src.Interprete.simbol.RaizArbol import Arbol
from backend.src.Interprete.visitor_object.visitor_output import Visitor_Output

BlueprintParse = Blueprint('parse', __name__)

#!RUTA: http://localhost:4000/
@BlueprintParse.route('/api/parse', methods=['POST'])
def prueba():
    # Accede al contenido JSON enviado por el frontend
    data = request.get_json()
    if not data or 'input' not in data:
        return jsonify({'error': 'No input provided'}), 400

    input = data['input']
    print(f"Input recibido: {input['code']}")

    # SE OBTIENE EL AST CREADO POR EL PARSER
    try:
        instrucciones = parser.parse(input['code'])
        print(instrucciones)
        ast = Arbol(instrucciones)
    except Exception as e:
        print(f"Error al crear el árbol")
        print(f"Error: {str(e)}")
        return jsonify({'error': str(e)}), 500

    if ast is None: 
        print("Hubo un error al parsear la expresión.")
        return jsonify({'error': 'Error al parsear la expresión.'}), 500
    
    print("AST generado correctamente.")
    visitor = Visitor_Output(ast)

    # SE IMPRIME EL AST
    for nodo in ast.getInstrucciones():
        nodo.accept(visitor)

    print(ast.getConsola())
    return jsonify({'consola': ast.getConsola()})