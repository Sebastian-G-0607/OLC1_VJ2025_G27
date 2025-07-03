import os

from backend.src.Interprete.nodes.instrucciones.Execute import Execute
from backend.src.Interprete.nodes.instrucciones.Procedimiento import Procedimiento
from backend.src.Interprete.simbol.RaizArbol import Arbol

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
vectores_html_path = os.path.join(PROJECT_ROOT, 'public', 'vectores', 'reporteVectores.html')

from flask import Blueprint, jsonify, request, send_file
from backend.src.Interprete.simbol.InstanciaTabla import st
from backend.src.Interprete.parser import parse
from backend.src.Interprete.simbol.ListaErrores import errores
from backend.src.Interprete.visitor_object.visitor_output import Visitor_Output

BlueprintVectores = Blueprint('reporte_vectores', __name__)

@BlueprintVectores.route('/reporte/vectores', methods=['GET'])
def generar_reporteVectores():
    global st
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

    with open(vectores_html_path, 'w') as file:
        file.write('<html><head><title>Reporte de Tabla de Vectores</title>')
        file.write(css)
        file.write('</head><body>')

        file.write('<h1>Reporte de Tabla de Vectores</h1>')
        file.write('<table border="0"><tr><th>Nombre</th><th>Tipo de ordenamiento</th><th>Tipo de Dato</th><th>Valor</th><th>Alcance</th><th>Fila</th><th>Columna</th></tr>')

        # Valida si hay simbolos antes de generar el reporte
        if not any(symbol.entity_type == 'vector' for symbol in st.symbols):
            file.write('<tr><td colspan="7">No hay vectores en la tabla.</td></tr>')
            file.write('</table></body></html>')
        
        else:
            # Si hay símbolos, se procede a generar el reporte
            for simbolo in st.symbols:
                if simbolo.entity_type == 'vector':
                    file.write(f'<tr><td>{simbolo.name}</td><td>{simbolo.ordenamiento}</td><td>{simbolo.data_type}</td>')
                    file.write(f'<td>{simbolo.value}</td><td>{simbolo.scope}</td><td>{simbolo.line}</td><td>{simbolo.column}</td></tr>')

        file.write('</table></body></html>')
    return send_file(vectores_html_path, mimetype='text/html')