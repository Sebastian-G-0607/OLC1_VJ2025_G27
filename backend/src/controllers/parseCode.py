import os

from graphviz import Source
from ply import yacc
from flask import Blueprint, jsonify, request, send_file
from backend.src.Interprete.visitor_object.visitor_graph import VisitorGraph
from backend.src.Interprete.simbol.RaizArbol import Arbol
from backend.src.Interprete.visitor_object.visitor_output import Visitor_Output
from backend.src.Interprete.simbol.ListaErrores import errores
from backend.src.Interprete.simbol.InstanciaTabla import st
from backend.src.Interprete.parser import parse

def build_parser():
    from backend.src.Interprete.parser import parser
    return yacc.yacc(module=parser)

BlueprintParse = Blueprint('parse', __name__)

#!RUTA: http://localhost:4000/
@BlueprintParse.route('/api/parse', methods=['POST'])
def prueba():

    #Limpiar la lista de errores antes de cada petición
    errores.clear()
    #Limpia la tabla de simbolos antes de cada petición
    global st
    st.clear()

    ast = None
    data = None
    instrucciones = None

    # Accede al contenido JSON enviado por el frontend
    data = request.get_json()
    if not data or 'input' not in data:
        return jsonify({'error': 'No hay contenido para interpretar'}), 400

    input = data['input']

    # SE OBTIENE EL AST CREADO POR EL PARSER
    try:
        instrucciones = parse(input['code'])
        ast = Arbol(instrucciones)
    except Exception as e:
        print(f"Error al crear el árbol")
        print(f"Error: {str(e)}")
        return jsonify({'error': 'Ocurrió un error al crear el AST'}), 500

    if ast is None: 
        print("Hubo un error al parsear la expresión.")
        return jsonify({'error': 'Error al parsear la expresión.'}), 500
    
    print("AST generado correctamente.")
    visitor = Visitor_Output(ast)

    # SE IMPRIME EL AST
    if ast.getInstrucciones() is None:
        print("El AST no contiene instrucciones.")
        return jsonify({'error': 'El AST no contiene instrucciones.'}), 500
    try:
        for nodo in ast.getInstrucciones():
                nodo.accept(visitor)
    except Exception as e:
        print(f"Error al visitar el AST: {str(e)}")
        return jsonify({'error': 'Ocurrió un error al visitar el AST'}), 500

    # SE IMPRIME LA TABLA DE SIMBOLOS
    st.print_table()

    # SE IMPRIMEN LOS ERRORES SI HAY
    if errores:
        print("Errores encontrados:")
        for error in errores:
            print(error)

    return jsonify({'consola': ast.getConsola()})

@BlueprintParse.route('/api/ast', methods=['POST'])
def reporte_ast():
    data = request.get_json()
    if not data or 'input' not in data:
        return jsonify({'error': 'No input provided'}), 400

    input = data['input']

    try:
        instrucciones = parse(input['code'])
        ast = Arbol(instrucciones)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    visitor_gv = VisitorGraph(ast)
    # SE IMPRIME EL AST
    if ast.getInstrucciones() is None:
        print("El AST no contiene instrucciones.")
        return jsonify({'error': 'El AST no contiene instrucciones.'}), 500
    try:
        for nodo in ast.getInstrucciones():
                codigo = nodo.accept(visitor_gv)
                visitor_gv.dot.append(codigo)
    except Exception as e:
        print(f"Error al visitar el AST: {str(e)}")
        return jsonify({'error': 'Ocurrió un error al visitar el AST'}), 500
    dot_ast = visitor_gv.generar_dot(ast)

# Ruta absoluta a la carpeta src
    src_dir = os.path.dirname(os.path.abspath(__file__))  # controllers
    src_dir = os.path.dirname(src_dir)  # src

    dot_path = os.path.join(src_dir, "ast.dot")
    svg_path = os.path.join(src_dir, "ast.svg")

    # Guardar DOT en src
    with open(dot_path, "w", encoding="utf-8") as f:
        f.write(dot_ast)

    # Generar SVG en src
    src_graph = Source(dot_ast)
    src_graph.render(filename="ast", directory=src_dir, format='svg', cleanup=True)

    # Devuelve el archivo SVG
    return send_file(svg_path, mimetype='image/svg+xml', as_attachment=True, download_name='ast.svg')