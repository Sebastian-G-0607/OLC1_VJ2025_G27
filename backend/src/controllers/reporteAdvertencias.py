import os

from backend.src.Interprete.nodes.instrucciones.Execute import Execute
from backend.src.Interprete.nodes.instrucciones.Procedimiento import Procedimiento
from backend.src.Interprete.simbol.RaizArbol import Arbol

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
advertencias_html_path = os.path.join(PROJECT_ROOT, 'public', 'advertencias', 'reporteAdvertencias.html')

from flask import Blueprint, jsonify, request, send_file
from backend.src.Interprete.simbol.InstanciaTabla import st
from backend.src.Interprete.parser import parse
from backend.src.Interprete.simbol.ListaErrores import errores
from backend.src.Interprete.visitor_object.visitor_output import Visitor_Output

BlueprintAdvertencias = Blueprint('reporte_advertencias', __name__)

@BlueprintAdvertencias.route('/api/reporte/advertencias', methods=['POST'])
def generar_reporteAdvertencias():

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
        return jsonify({'error': 'Ocurrió un error al crear el AST durante el reporte de advertencias'}), 500

    if ast is None: 
        print("Hubo un error al parsear la expresión durante el reporte de advertencias.")
        return jsonify({'error': 'Error al parsear la expresión durante el reporte de advertencias.'}), 500

    print("AST generado correctamente.")
    visitor = Visitor_Output(ast)

    # SE IMPRIME EL AST
    if ast.getInstrucciones() is None:
        print("El AST no contiene instrucciones.")
        return jsonify({'error': 'El AST no contiene instrucciones para el reporte de advertencias.'}), 500
    try:
        for nodo in ast.getInstrucciones():
            try:
                nodo.accept(visitor)
            except TypeError as e:
                if "NoneType" in str(e):
                    continue  # Ignora y sigue con el siguiente nodo
                else:
                    raise  # Si es otro TypeError, relanza la excepción
    except Exception as e:
        print(f"Error al visitar el AST: {str(e)}")
        return jsonify({'error': 'Ocurrió un error al visitar el AST'}), 500

    try:
        # CSS PARA EL REPORTE HTML
        css = """
            <style>
                body {
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background: #f7fafc;
                    color: #22223b;
                    margin: 0;
                    padding: 0;
                }
                h1 {
                    text-align: center;
                    color: #3a5a40;
                    margin-top: 32px;
                    margin-bottom: 24px;
                }
                table {
                    margin: 0 auto 40px auto;
                    border-collapse: collapse;
                    width: 90%;
                    background: #fff;
                    box-shadow: 0 2px 8px rgba(58, 90, 64, 0.08);
                    border-radius: 8px;
                    overflow: hidden;
                }
                th, td {
                    padding: 12px 16px;
                    text-align: left;
                }
                th {
                    background: #a3b18a;
                    color: #fff;
                    font-weight: 600;
                    border-bottom: 2px solid #588157;
                }
                tr:nth-child(even) {
                    background: #f0efeb;
                }
                tr:nth-child(odd) {
                    background: #fff;
                }
                tr:hover {
                    background: #d8f3dc;
                }
                td {
                    border-bottom: 1px solid #e9ecef;
                }
            </style>"""
        with open(advertencias_html_path, 'w') as file:
            file.write('<html><head><title>Reporte de Tabla de Advertencias</title>')
            file.write(css)
            file.write('</head><body>')

            file.write('<h1>Reporte de Tabla de Advertencias</h1>')
            file.write('<table border="0"><tr><th>Procedimiento</th><th>Mensaje</th><th>Linea</th><th>Columna</th>')

            # Valida si hay advertencias antes de generar el reporte
            if not any(adv for adv in ast.getAdvertencias()):
                file.write('<tr><td colspan="7">No hay advertencias en la tabla.</td></tr>')
                file.write('</table></body></html>')
            
            else:
                # Si hay advertencias, se procede a generar el reporte
                for adv in ast.getAdvertencias():
                    file.write(f'<tr><td>{adv.procedimiento}</td><td>{adv.mensaje}</td><td>{adv.linea}</td><td>{adv.columna}</td></tr>')

            file.write('</table></body></html>')
        
        return send_file(advertencias_html_path, mimetype='text/html')

    except Exception as e:
        print(f"Error al generar el reporte de advertencias: {str(e)}")
        return jsonify({'error': 'Ocurrió un error al generar el reporte de advertencias.'}), 500