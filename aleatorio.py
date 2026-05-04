import random

locais = {

    1: "Aquario",
    2: "boliche",
    3: "Praça XV",
    4: "Feira Da Gloria",
    5: "Dorama Food"

}

local = random.randint(1,5)
print(f"O local escolhido foi {locais[local]}")