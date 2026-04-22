#Projeto dedicado a automatização de contas, calculos.  
bs = input ("Qual seria seu objetivo ?")

if bs == "decimal":
    print("Você escolheu converter para decimal.")
elif bs == "binario":
    print("Você escolheu converter para binário.")
elif bs == "octal":
    print("Você escolheu converter para octal.")
elif bs == "hexadecimal":
    print("Você escolheu converter para hexadecimal.")
else:
    print("Objetivo inválido.")

n1 = int(input("Digite um numero: "))

if bs == "decimal":
    print("O numero em decimal é ", n1)
elif bs == "binario":
    print("O numero em binário é ", bin(n1))
elif bs == "octal":
    print("O numero em octal é ", oct(n1))
elif bs == "hexadecimal":
    print("O numero em hexadecimal é ", hex(n1))
else:
    print("Objetivo inválido.")

n2 = int(input("Digite outro numero: "))
if bs == "decimal":
    print("O numero em decimal é ", n2)
elif bs == "binario":
    print("O numero em binário é ", bin(n2))
elif bs == "octal":
    print("O numero em octal é ", oct(n2))
elif bs == "hexadecimal":
    print("O numero em hexadecimal é ", hex(n2))
else:
    print("Objetivo inválido.")

if bs == "decimal": 10^2