class Funcionario:
    def __init__(self, nome, salario):
        self.nome =  nome
        self.salario = salario

    def apresentar(self):
        return f"Nome: {self.nome}, Salário Total: R$ {self.salario}"
    
class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome,salario)
        self.bonus = bonus

    def apresentar(self):
        total = self.salario + self.bonus
        return f"Nome: {self.nome}, Salário: R$ {total:.2f}"

class Estagiario(Funcionario):
    def __init__(self, nome, salario, curso):
        super().__init__(nome, salario)
        self.curso = curso
    
    def apresentar(self):
        total = self.salario * 0.5
        return f"Nome: {self.nome}, Salário: R$ {self.salario:.2f}, Curso: {self.curso}"

a1 = Gerente("João", 5000, 2000)
a2 = Estagiario("Maria", 2000, "Engenharia de Software")
a3 = Funcionario("Pedro", 3000)
a4 = Gerente("Ana", 6000, 2500)
a5 = Estagiario("Carlos", 1500, "Design Gráfico")

funcionarios = a1, a2, a3, a4, a5

for f in funcionarios:
    print(f.apresentar())
