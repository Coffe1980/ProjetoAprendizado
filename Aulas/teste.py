import random
ranking = []

def dificuldade():
    nome = input("Qual seu nome ? ")

    while True:
        dificuldade = input(
            "Qual dificuldade deseja jogar (Facil, Medio ou dificil.) \n Lembrando, toda dificuldade terá limite de tentativas! "
        ).lower()

        if dificuldade == "facil":
            numero_secreto = random.randint(1, 50)
            limite = 50
            pf = 2
            max_tentativas = 10

        elif dificuldade == "medio":
            numero_secreto = random.randint(1, 100)
            limite = 100
            pf = 5
            max_tentativas = 7

        elif dificuldade == "dificil":
            numero_secreto = random.randint(1, 150)
            limite = 150
            pf = 10
            max_tentativas = 5

        else:
            print("Dificuldade invalida, tente novamente!")
            continue  # 🔥 volta pro início do loop

        return nome, numero_secreto, limite, max_tentativas, pf
    
def jogar(nome, numero_secreto, limite, max_tentativas, pf):

    print(f"Olá! {nome} Bem vindo! \n Tente adivinhar o numero de 1 até {limite}")

    tentativa = 0
    acertou = False

    while not acertou and tentativa < max_tentativas:

        # 🔹 VALIDAÇÃO DO INPUT
        while True:
            chute = input("Digite um numero: ")
            try:
                chute = int(chute)
                if chute < 1 or chute > limite:
                    print(f"Por favor, digite um numero entre 1 e {limite}.")
                    continue
                break  # 🔥 sai do loop quando o número é válido
            except ValueError:
                print("Entrada inválida. Digite um número válido.")

        # 🔹 CÁLCULO
        tentativa += 1
        restante = max_tentativas - tentativa
        pontos = restante * pf

        print(f"Restam {restante} tentativas")

        # 🔹 LÓGICA DO JOGO
        if chute == numero_secreto:
            print(f"{nome}, parabéns! você acertou em {tentativa} tentativas")
            return nome, tentativa, pontos

        elif chute < numero_secreto:
            print("O numero é maior!")

        else:
            print("O numero é menor!")

    # 🔹 PERDEU
    print(f"Você perdeu! O número era {numero_secreto}")
    return None
while True:
    dados = dificuldade()
    resultado = jogar(*dados)

    if resultado:
        ranking.append(resultado)
        ranking.sort(key=lambda x: x[2], reverse=True)

        print("======== RANKING ========")
        for i, (nome, tentativas, pontos) in enumerate(ranking, start=1):
            print(f"{i}. {nome} - {tentativas} tentativas - {pontos} pontos")

    repeat = input("Quer continuar? ").strip().lower()

    if repeat not in ("sim", "s", "yes"):
        break

print("Espero que tenha gostado 👌")