from flask import Flask, jsonify, render_template, request
import json
from jogo import Jogo

app = Flask(__name__)

jogo_atual = Jogo()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ranking')
def get_ranking():
    try:
        with open('ranking.json', 'r') as f:
            dados = json.load(f)
            return jsonify(dados)
    except FileNotFoundError:
        return jsonify({"ranking": [], "data": ""})

@app.route('/iniciar', methods=['POST'])
def iniciar():
    dados = request.get_json()
    nivel = dados.get('nivel')
    jogo_atual.iniciar(nivel)
    return jsonify({
        "limite": jogo_atual.limite,
        "max_tentativas": jogo_atual.max_tentativas
    })

@app.route('/chutar', methods=['POST'])
def chutar():
    dados = request.get_json()
    numero = int(dados.get('numero'))
    resultado = jogo_atual.chutar(numero)
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)