import random

print ('----BLACK JACK----')
baralho =[
    {'nome': 'Rei',    'valor': 10},
    {'nome': 'Dama',   'valor': 10},
    {'nome': 'Valete', 'valor': 10},
    {'nome': '2', 'valor': 2},
    {'nome': '3', 'valor': 3},
    {'nome': '4', 'valor': 4},
    {'nome': '5', 'valor': 5},
    {'nome': '6', 'valor': 6},
    {'nome': '7', 'valor': 7},
    {'nome': '8', 'valor': 8},
    {'nome': '9', 'valor': 9},
    {'nome': 'As', 'valor': 11}

]
random.shuffle(baralho)
mao_jogador = [baralho[0], baralho[1]]

print(baralho[0])
print(baralho[0]['nome'])
print(mao_jogador)