from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def greeting():
    return "Hello World!"

@app.route('/hello2')
def greeting2():
    return "Hello World! Part 2"

@app.route('/ParticipacionElectoral/participacion')
def get_participacion_electoral():
    return "ParticipacionElectoral"

if __name__ == "__main__":
    app.run(debug=True)