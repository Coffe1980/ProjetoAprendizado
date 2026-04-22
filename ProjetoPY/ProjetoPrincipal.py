import random
import json
import time
import threading
from datetime import datetime

# Função para carregar e mostrar ranking

def vinte_e_quatro_horas(data):
    diferenca = datetime.now() - datetime.fromisoformat(data)
    if diferenca.total_seconds() / 3600 > 24:
        return True
    return False

def verificar__conquistas(pontos, conquistas_usuario):
                            for conquista, valor in conquistas.items():
                                if pontos >= valor and conquista not in conquistas_usuario:
                                    print(f"Parabens você ganhou uma conquista {conquista} por alcançar {pontos} pontos!")
                                    conquistas_usuario.append(conquista)

def carregar_ranking():
    try:
        with open("ranking.json", "r") as arquivo:
            dados_salvo = json.load(arquivo)
            ranking = dados_salvo["ranking"]
            data = dados_salvo["data"]
            resetou = False
            if vinte_e_quatro_horas(data):
                ranking = []
                resetou = True
                print("O ranking foi resetado, pois já se passaram 24 horas desde a última atualização.")
    except FileNotFoundError:
        ranking = []
        resetou = False  # Se o arquivo não existir, cria lista vazia

    ver = input("Quer ver o ranking S/N ? ").strip().lower()
    if ver in ("sim", "s", "ss", "yes", "y", "claro", "sempre"):
        if not ranking:
            print("Ranking vazio!")
        else:
            print("\n--- Ranking ---")
            for i, usuario in enumerate(ranking, start=1):
                print(f"{i}. {usuario['nome']} - dificuldade: {usuario['dificuldade']} - {usuario['partidas_jogadas']} partidas - {usuario['pontos']} pontos {' '.join(c[0] for c in usuario['conquistas'])}")
            print("----------------\n")
    return ranking, resetou

def input_com_tempo():
    return input("Digite um número: ")


# Função para obter o nome do usuário
def obter_nome():
    while True:
                
            nome = input("Qual seu nome? ").strip().lower()
            if not nome:
                print("Nome invalido!")
                continue
            print(f"Bem vindo {nome}")
            return nome

# Função para escolher dificuldade
def dificuldade(nome):
    while True:
        nivel = input(
            "Qual dificuldade deseja jogar (Facil, Medio ou Dificil)?\n"
            "Lembrando, cada dificuldade terá limite de tentativas: "
        ).lower()

        if nivel == "facil":
            numero_secreto = random.randint(1, 50)
            limite = 50
            pf = 5
            max_tentativas = 12
        elif nivel == "medio":
            numero_secreto = random.randint(1, 100)
            limite = 100
            pf = 10
            max_tentativas = 10
        elif nivel == "dificil":
            numero_secreto = random.randint(1, 150)
            limite = 150
            pf = 20
            max_tentativas = 8
        else:
            print("Dificuldade inválida, tente novamente!")
            continue

        return nome, numero_secreto, limite, max_tentativas, nivel, pf

# Função do jogo
def jogar(nome, numero_secreto, limite, max_tentativas, dificuldade, pf):
    print(f"\nOlá {nome}! Tente adivinhar o número de 1 até {limite}")

    limite_inferior =  1
    limite_superior = limite
    tentativa = 0
    while tentativa < max_tentativas:
        while True:
            inicio =  time.time()
            chute = input("Digite um número: ")
            fim = time.time()
            tempo_gasto = fim - inicio
            if tempo_gasto > 30:
                print("Tempo esgotado! Você perdeu uma tentativa.")
                tentativa += 1
                continue
            try:
                chute = int(chute)
                if chute < 1 or chute > limite:
                    print(f"Digite um número entre 1 e {limite}.")
                    continue
                break
            except ValueError:
                print("Entrada inválida. Digite um número válido.")
        
        tentativa += 1
        restante = max_tentativas - tentativa
        pontos = restante * pf
        abs_chute = abs(chute - numero_secreto)

        print(f"Restam {restante} tentativas")

        if chute == numero_secreto:
            print(f"Parabéns, {nome}! Você acertou em {tentativa} tentativas!\n")   
            return nome, tentativa, pontos
        
        if chute > numero_secreto:
            limite_superior =  chute
        else:
            limite_inferior = chute
        if tentativa >= 3:
            print(f"Dica o numero está entre {limite_inferior} e {limite_superior}")
        if abs_chute > 10:
            print("Está um pouco longe 😕")
        elif abs_chute > 5:
            print("Está perto! 😎")
        elif abs_chute > 2:
            print("Está muito perto! 🥵")
        else:
            print("Quase! Do seu lado 😅")

    print(f"Você perdeu! O número era {numero_secreto}\n")
    return None

# Loop principal do jogo
primeira_vez =  True
pf_conquista = 1
conquistas = {
    "🥉 Bronze": 50,
    "🥈 Prata": 100,
    "🥇 Ouro": 300,
    "💎 Diamante": 500
}

while True:
        if primeira_vez:
            nome = obter_nome()
            data = datetime.now().isoformat()
            ranking, resetou = carregar_ranking()
            if resetou:
                dados_salvo = {"data": data, "ranking": ranking}
                with open("ranking.json", "w") as arquivo:
                    json.dump(dados_salvo, arquivo, indent=4)
            primeira_vez = False
        dados = dificuldade(nome)
        resultado = jogar(*dados)
        data = datetime.now().isoformat()

        if resultado:
            nome, tentativas, pontos = resultado
            encontrado = False
            for usuario in ranking:
                if usuario['nome'] == nome and usuario['dificuldade'] == dados[4]:
                    usuario['pontos'] += pontos
                    usuario['partidas_jogadas'] += 1
                    if dados[4] in ("medio", "dificil"):
                        pf_conquista += pontos
                        verificar__conquistas(pf_conquista, usuario['conquistas'])
                    encontrado = True
                    print(f"Ganhou mais {pontos} pontos!")
            if not encontrado:
                ranking.append ({"nome": nome, "partidas_jogadas": 1, "pontos": pontos, "dificuldade": dados[4], "conquistas":[]})
            ranking.sort(key=lambda x: x["pontos"], reverse=True)
            print("\n--- Ranking Atualizado ---")
            for i, usuario in enumerate (ranking, start=1):
                print(f"{i}. {usuario['nome']} - dificuldade: {usuario['dificuldade']} - {usuario['partidas_jogadas']} partidas - {usuario['pontos']} pontos {' '.join(c[0] for c in usuario['conquistas'])}")
            print("----------------\n")

            dados_salvo = {
            "data": data,
            "ranking": ranking
            }

            # Salvar ranking no arquivo JSON
            with open("ranking.json", "w") as arquivo:
                json.dump(dados_salvo, arquivo, indent=4)

        repeat = input("Quer jogar novamente? S/N ").strip().lower()
        if repeat not in ("sim", "s", "yes", "y", "claro", "com certeza"):
            break

print("Espero que tenha gostado 👌")