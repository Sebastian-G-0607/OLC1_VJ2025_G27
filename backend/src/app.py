import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(PROJECT_ROOT)  # Añade /OLC1_VJ2025_G27

from flask import Flask, send_file

from backend.src.controllers.parseCode import BlueprintParse
from backend.src.controllers.reporteErrores import BlueprintErrors
from backend.src.controllers.reporteTS import BlueprintST

app = Flask(__name__)

app.register_blueprint(BlueprintParse)
app.register_blueprint(BlueprintErrors)
app.register_blueprint(BlueprintST)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)