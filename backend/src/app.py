import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(PROJECT_ROOT)  # Añade /OLC1_VJ2025_G27

from flask import Flask 
from backend.src.controllers.prueba import BlueprintPrueba

app = Flask(__name__)

app.register_blueprint(BlueprintPrueba)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)
    