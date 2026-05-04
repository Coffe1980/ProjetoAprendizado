from operator import truediv

from flask import Flask, jsonify, render_template, request
import json

from flask.cli import F
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
        "max_tentativas": jogo_atual.max_tentativas,
        "nivel": jogo_atual.nivel
    })

@app.route('/chutar', methods=['POST'])
def chutar():
    dados = request.get_json()
    numero = int(dados.get('numero'))
    resultado = jogo_atual.chutar(numero)
    return jsonify(resultado)

@app.route('/salvar_ranking', methods=['POST'])
def salvar_ranking():
    from datetime import datetime
    dados = request.get_json()
    try:
        with open('ranking.json', 'r') as f:
            ranking_atual = json.load(f)
    except FileNotFoundError:
        ranking_atual = {"ranking": [], "data": ""}

    ranking = ranking_atual.get("ranking", [])
    nome = dados.get("nome")
    nivel = dados.get("nivel")
    pontos = dados.get("pontos")

    encontrado =  False
    for usuario in ranking:
        if usuario["nome"] == nome and usuario ["dificuldade"] ==  nivel:
            usuario["pontos"] += pontos
            usuario["partidas_jogadas"] += 1
            encontrado = True


    if not encontrado:
        ranking.append({"nome": nome, "pontos": pontos, "partidas_jogadas": 1, "dificuldade": nivel, "conquistas": []})

    ranking.sort(key=lambda x: x["pontos"], reverse=True)

    with open ('ranking.json', 'w') as f:
        json.dump({"ranking": ranking, "data": datetime.now().isoformat() },f, indent=4)

    return jsonify({"ranking": ranking})


if __name__ == '__main__':
    app.run(debug=True)