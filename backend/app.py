from flask import Flask 
from src.controllers.prueba import BlueprintPrueba



app = Flask(__name__)

app.register_blueprint(BlueprintPrueba)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)