import random

class Jogo:
    def __init__(self):
        self.numero_secreto = 0
        self.tentativas = 0
        self.max_tentativas = 0
        self.limite = 0
        self.pf = 0
        self.nivel = ''
        self.ativo = False

    def iniciar(self, nivel):
        if nivel == 'facil':
            self.numero_secreto = random.randint(1, 50)
            self.limite = 50
            self.max_tentativas = 12
            self.pf = 5
        elif nivel == 'medio':
            self.numero_secreto = random.randint(1, 100)
            self.limite = 100
            self.max_tentativas = 10
            self.pf = 10
        elif nivel == 'dificil':
            self.numero_secreto = random.randint(1, 150)
            self.limite = 150
            self.max_tentativas = 8
            self.pf = 20

        self.tentativas = 0
        self.nivel = nivel
        self.ativo = True

    def chutar(self, numero):
        if not self.ativo:
            return {"resultado": "jogo_inativo"}

        self.tentativas += 1
        restante = self.max_tentativas - self.tentativas
        pontos = restante * self.pf
        diferenca = abs(numero - self.numero_secreto)

        if numero == self.numero_secreto:
            self.ativo = False
            return {"resultado": "ganhou", "pontos": pontos, "tentativas": self.tentativas}

        if self.tentativas >= self.max_tentativas:
            self.ativo = False
            return {"resultado": "perdeu", "numero_secreto": self.numero_secreto}

        if diferenca > 10:
            dica = "Está um pouco longe 😕"
        elif diferenca > 5:
            dica = "Está perto! 😎"
        elif diferenca > 2:
            dica = "Está muito perto! 🥵"
        else:
            dica = "Quase! Do seu lado 😅"

        direcao = "O número é menor! 👇" if numero > self.numero_secreto else "O número é maior! 👆"

        return {"resultado": "continua", "dica": dica, "direcao": direcao, "restante": restante}

