class aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
        
    def media(self):
        return sum(self.nota) / len(self.nota)
    def situacao(self):
        if self.media() >= 7:
            return "Aprovado"
        elif self.media() >= 5:
            return "Recuperação"
        else:
            return "Reprovado"
    
    a1 = aluno("João", [1,3,5,7])
    a2 = aluno("Maria", [1,3,5,7])
    a3 = aluno("Pedro", [1,3,5,7])
    
    aluno = [a1, a2, a3]

    for a in aluno:
        print(f"Aluno: {a.nome}, Média: {a.media()}, Situação: {a.situacao()}")