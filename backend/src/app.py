import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(PROJECT_ROOT)  # Añade /OLC1_VJ2025_G27

from flask import Flask, send_file

from backend.src.controllers.parseCode import BlueprintParse

app = Flask(__name__)

app.register_blueprint(BlueprintParse)

@app.route('/reporte/errores', methods=['GET'])
def reporte_errores():
    from backend.src.controllers.reporteErrores import generar_reporteErrores
    
    generar_reporteErrores()  # Solo genera el archivo, no retorna nada

    return send_file('backend/src/controllers/reporteErrores.html', mimetype='text/html')

@app.route('/reporte/simbolos', methods=['GET'])
def reporte_simbolos():
    from backend.src.controllers.reporteTS import generar_reporteTS

    # Genera el reporte de la tabla de símbolos
    generar_reporteTS()
    
    # Retorna el archivo HTML generado
    return send_file('backend/src/controllers/reporteTS.html', mimetype='text/html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)