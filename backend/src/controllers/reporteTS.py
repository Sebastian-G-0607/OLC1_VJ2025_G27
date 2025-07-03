import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
st_html_path = os.path.join(PROJECT_ROOT, 'public', 'symbol', 'reporteTS.html')

from flask import Blueprint, send_file
from backend.src.Interprete.simbol.InstanciaTabla import st

BlueprintST = Blueprint('symbol_table', __name__)

@BlueprintST.route('/reporte/simbolos', methods=['GET'])
def generar_reporteTS():
    """
    Crear reporte html de la tabla de simbolos
    """
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
    </style>
    """

    with open(st_html_path, 'w') as file:
        file.write('<html><head><title>Reporte de Tabla de Símbolos</title>')
        file.write(css)
        file.write('</head><body>')

        file.write('<h1>Reporte de Tabla de Símbolos</h1>')
        file.write('<table border="0"><tr><th>Nombre</th><th>Tipo de Entidad</th><th>Tipo de Dato</th><th>Valor</th><th>Alcance</th><th>Fila</th><th>Columna</th></tr>')

        # Valida si hay simbolos antes de generar el reporte
        if not st.symbols:
            file.write('<tr><td colspan="7">No hay símbolos en la tabla.</td></tr>')
            file.write('</table></body></html>')
        
        else:
            # Si hay símbolos, se procede a generar el reporte
            for simbolo in st.symbols:
                file.write(f'<tr><td>{simbolo.name}</td><td>{simbolo.entity_type}</td><td>{simbolo.data_type}</td>')
                file.write(f'<td>{simbolo.value}</td><td>{simbolo.scope}</td><td>{simbolo.line}</td><td>{simbolo.column}</td></tr>')

        file.write('</table></body></html>')
    return send_file(st_html_path, mimetype='text/html')