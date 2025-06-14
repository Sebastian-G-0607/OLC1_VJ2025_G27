from flask import Blueprint, jsonify, request
from backend.src.Interprete.parser import parser
from backend.src.Interprete.simbol.RaizArbol import Arbol
from backend.src.Interprete.visitor_object.visitor_output import Visitor_Output
from backend.src.Interprete.simbol.ListaErrores import errores
from backend.src.Interprete.simbol.InstanciaTabla import st

BlueprintParse = Blueprint('parse', __name__)

#!RUTA: http://localhost:4000/
@BlueprintParse.route('/api/parse', methods=['POST'])
def prueba():
    #parser.clear()  # Limpiar el parser antes de cada petición
    #Limpiar la lista de errores antes de cada petición
    errores.clear()
    #Limpia la tabla de simbolos antes de cada petición
    global st
    st.clear()

    ast = None
    data = None

    # Accede al contenido JSON enviado por el frontend
    data = request.get_json()
    if not data or 'input' not in data:
        return jsonify({'error': 'No input provided'}), 400

    input = data['input']

    # SE OBTIENE EL AST CREADO POR EL PARSER
    try:
        instrucciones = parser.parse(input['code'])
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

    # SE IMPRIME LA TABLA DE SIMBOLOS
    st.print_table()
    
    # SE IMPRIMEN LOS ERRORES SI HAY
    if errores:
        print("Errores encontrados:")
        for error in errores:
            print(error)

    return jsonify({'consola': ast.getConsola()})