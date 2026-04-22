
"""""
print ("hello world")
nome = input("Qual é o seu nome? ")
print ("Olá, " + nome + "!")
idade = input("Quantos anos você tem? ")
print ("Você tem " + idade + " anos.")
idade = int(idade)
if idade >= 18:
        print ("Você é maior de idade.")
else:    print ("Você é menor de idade.")
"""
#from wsgiref.validate import check_input
"""""
print ("Fala comigo bebe")
nome = input("Qual seu nome ?")
print ("Nossa que legal seu nome é", nome)
print ("Agora eu preciso que você me fale 2 numeros!")
n1 = int(input ("primeiro numero: " ))
n2 = int(input ("segundo numero: " ))
s = n1 + n2
print ("Então seus dois numeros foram", n1, "e", n2, "?")
# print ("A soma entre esses dois numeros é", s)
print("A soma entre {0} e {1} vale {2}".format( n1, n2, s))     
"""
# Primeiro exercicio e segundo exercicio
"""""
print("hello world")
name = input("What is your name? ")
print("Hello " + name + "!")
# Terceiro exercicio
n1 = int(input("Enter a number: "))
n2 = int(input("Enter another number: "))
print ("The sum of {0} and {1} is {2}".format(n1, n2, n1 + n2))
"""

# Quarto exercicio
"""
a =  input("Digite Algo: ")
print ("O tipo primitivo desse valor é ", type (a))
print ("Só tem espeaços?",  a.isspace())
print ("É um numero?", a.isnumeric())
print ("é alfabetico?", a.isalpha())
print ("é alfanumerico?", a.isalnum())
print ("ésta em maaiuscula ?", a.isupper())
print ("Está em minuscula ?", a.islower())
print ("está capitalizadaa ?",  a.istitle())
print ("O valor digitado é ", a.format(a)) 
"""

#> Calculadora
# + Adição, - Subtração, * Multiplicação, / Divisão, // Divisão inteira, % Resto da divisão, ** Potência
#Ordem de precedencia: 1. (), 2. **, 3. *, /, //, %, 4. +, -
""""
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
resposta = input ("O que você deseja fazer com esses numeros ? +, -, *, /, //, %, **: ")
if resposta == "+":
    print ("A soma entre os numeros é ", n1 + n2)
elif resposta == "-":
    print ("A subtração entre os numeros é ", n1 - n2  )
elif resposta == "*":
    print ("A multiplicação entre os numeros é ", n1 * n2)
elif resposta == "/":
    print ("A divisão entre os numeros é ", n1 / n2)
elif resposta == "//":
    print ("A divisão inteira entre os numeros é ", n1 // n2)
elif resposta == "%":
    print ("O resto da divisão entre os numeros é ", n1 % n2)
elif resposta == "**":
    print ("A potência entre os numeros é ", n1 ** n2)
else :
    print ("Operação inválida")
    """

# Maneiras Variadas de colocar 
"""
`{:^} - Centralizado
`{:>} - Alinhado a direita
`{:<} - Alinhado a esquerda
"""
n = input ("Qual seu nome ? ")
print ("Olá, prazer em te conhecer {:>20}                                      !".format(n))
