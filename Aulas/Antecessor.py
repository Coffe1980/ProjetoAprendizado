# 1. PRIMEIRO — define a classe
class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def media(self):
        return sum(self.notas) / len(self.notas)

    def situacao(self):
        if self.media() >= 7:
            return "Aprovado"
        elif self.media() >= 5:
            return "Recuperação"
        else:
            return "Reprovado"

# 2. DEPOIS — usa a classe
a1 = Aluno("Ana",    [8, 9, 7, 10])
a2 = Aluno("Bruno",  [4, 6, 5, 3])
a3 = Aluno("Carla",  [6, 7, 5, 6])

alunos = [a1, a2, a3]

for aluno in alunos:
    print(f"{aluno.nome} — média: {aluno.media():.1f} — {aluno.situacao()}")