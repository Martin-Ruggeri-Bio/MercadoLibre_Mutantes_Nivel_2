from flask import Flask, request
from detector_de_mutantes import isMutant
from werkzeug.exceptions import abort

app = Flask(__name__)
app.secret_key = 'Mi_llave_secreta'


@app.route('/')
def inicio():
    return 'Esta es la pagina donde testearemos si eres mutante'

@app.route('/mutante', methods=['POST'])
def esMutante():
    dna = request.json['dna']
    if not isMutant(dna):
        abort(403)
    return f'El resultado es {isMutant(dna)}'
