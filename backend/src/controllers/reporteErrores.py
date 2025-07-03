import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
errores_html_path = os.path.join(PROJECT_ROOT, 'public', 'errores', 'reporteErrores.html')

from flask import Blueprint, send_file
from backend.src.Interprete.simbol.ListaErrores import errores

BlueprintErrors = Blueprint('errors', __name__)

@BlueprintErrors.route('/reporte/errores', methods=['GET'])
def generar_reporteErrores():
    """
    Crear reporte html de errores
    """
    with open(errores_html_path, 'w') as file:
        file.write('''<html>
            <head>
                <title>Reporte de Errores</title>
                <style>
                    body {
                        font-family: 'Segoe UI', Arial, sans-serif;
                        background: #f7f9fb;
                        color: #222;
                        margin: 0;
                        padding: 0;
                    }
                    h1 {
                        text-align: center;
                        margin-top: 40px;
                        color: #2d6cdf;
                        letter-spacing: 1px;
                    }
                    table {
                        margin: 40px auto;
                        border-collapse: collapse;
                        width: 80%;
                        background: #fff;
                        box-shadow: 0 2px 8px rgba(44, 62, 80, 0.08);
                        border-radius: 8px;
                        overflow: hidden;
                    }
                    th, td {
                        padding: 14px 18px;
                        text-align: left;
                    }
                    th {
                        background: #2d6cdf;
                        color: #fff;
                        font-weight: 600;
                        border-bottom: 2px solid #e3eaf2;
                    }
                    tr:nth-child(even) {
                        background: #f1f6fb;
                    }
                    tr:hover {
                        background: #eaf1fb;
                    }
                    td {
                        border-bottom: 1px solid #e3eaf2;
                    }
                    .no-errores {
                        text-align: center;
                        color: #888;
                        font-style: italic;
                    }
                </style>
            </head>
            <body>
            '''
        )

        file.write('<h1>Reporte de Errores</h1>')
        file.write('<table><tr><th>Tipo</th><th>Descripción</th><th>Fila</th><th>Columna</th></tr>')
        
        # Valida si hay errores antes de generar el reporte
        if not errores:
            file.write('<tr><td class="no-errores" colspan="4">No hay errores registrados.</td></tr>')
            file.write('</table></body></html>')
        
        else:
            for error in errores:
                file.write(f'<tr><td>{error.tipo}</td><td>{error.descripcion}</td><td>{error.linea}</td><td>{error.columna}</td></tr>')
        
        file.write('</table></body></html>')
    return send_file(errores_html_path, mimetype='text/html')



