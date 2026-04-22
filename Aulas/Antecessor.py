#Antecessor e Sucessor
"""
n1 = int(input ("Escolha um numero: "))
print ("O numero que você escolhe foi {:<20} " .format (n1))
print ("O numero é {} antecessor dele é {} e o sucesssor é {}".format (n1, (n1 - 2), (n1 + 2)))
 """
""""
# Dobro, Triplo e Raiz Quadrada.
n1 = int(input("Escolha um numero para saber seu dobro e seu triplo: "))
print ("O numero que você escolheu foi {} e seu dobro é {} e seu triplo é {} sua raiz é {:.3f} ".format (n1, n1*2, n1*3, n1**0.5))
"""

#Media Do Aluno
"""
n1 =  float(input ("Primeira nota "))
n2 =  float(input ("Segunda nota do aluno "))
m = (n1 + n2) /2
print ("A primeira nota do aluno foi {} e a segunda foi {} Sua media é {:.1f} ".format(n1, n2, m))
"""
"""
#Tabuada
n1 = int(input("Digite um numero para saber a tabuada dele "))
print ("O número escolhido foi {} sua tabuada é {}, {}, {}, {}, {}, {}, {}, {}, {}, {}" .format(n1, n1*1, n1*2, n1*3, n1*4, n1*5, n1*6, n1*7, n1*8, n1*9, n1*10))
 """
 #dolar pra real:

"""""
dolar = float(input("Quantos dolares você tem ? "))
dpr =  dolar * 5.25
print ("você tem ${} dolares e isso equivale a R$ {:,.2f} ".format(dolar, dpr))
"""
"""
#conversor de meidas:
medida = float(input("Digite uma medida em metros para saber a conversão em centimetros e milimetros: "))
dm = medida * 10
cm = medida * 100
mm = medida * 1000
km = medida / 1000
hm = medida * 100
dam = medida * 10

print("A medida de {} metros é equivalente a {} quilometros, {} hectometros, {} decametros, {:.0f} centimentros e {:0f} milimetros".format(medida, km, hm, dam, cm, mm))
"""
"""
#Pintando parede
parede = float (input("Qual a largura da parede ? "))
altura = float(input("Qual a altura da parede ? "))
area = parede * altura
tinta = area / 2
print ("A parede tem a dimenssão de {} x {} e sua area é de {} metros quadrados, para pintar essa parede você precisará de {} litros de tinta".format(parede, altura, area, tinta))

#Desconto
preço = float(input("Qual o preço da roupa ?" ))
desconto = preço * 0.05
print ("A roupa custa R${:.2F} mas com o desconto de 5% ela estará custando R${:.2F}".format(preço, preço - desconto))
"""
"""
#Aumento de salario
preço = float(input("Qual o salario do funcionário ? " ))
aumento = preço * 0.15
print ("O Funcionario irá ganhar um aumento de 15% e passará ganhar R${:.2f}".format(preço + aumento))

#Conversor de Temperatura
c = float(input("Qual é a temperatura em celsius ? "))
f = (9 * c)/5 + 32
print ("A temperatura de {}C é esquivalente a {}F ".format (c,f))

 #Aluguel de carro:
km = float(input("Quantos km você pecorreu com o carro ? "))
d = int(input("Quanto dias você ficou com o carro ? "))
diaria = 67 * d
kmr =  km * 0.15
total = diaria + kmr
print ("O valor da diaria foi R${:.2f} e o valor do km rodado foi R${:.1} o valor total a pagar é R${:.2f}".format(diaria, kmr, total))
"""