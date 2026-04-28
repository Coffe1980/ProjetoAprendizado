def soma(*numeros):
    return sum(numeros)

print(soma(1, 2, 3, 4))  # 10

def info(**dados):
    for k, v in dados.items():
        print((f"{k}: {v}"))

info(nome="Ana", idade=25)