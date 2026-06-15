fruta = input("Digite o nome de uma fruta: ")

frutas = {
    "Pera": 3.00,
    "Maçã": 2.50,
    "Banana": 1.80,
    "Laranja": 2.00,
    "Abacaxi": 4.00,
    "Limão": 1.50,
    "Uva": 3.50
}

if fruta in frutas:
    print(frutas[fruta])
else:
    print("Fruta não encontrada, entre com um valor válido.")


# Exercício 2

dados = {}

while True:
    frase = input("Digite uma frase: ")
    if frase == "":
        break
    
    if frase not in dados:
        dados[frase] = 1
    else:
        dados[frase] += 1

items = list(dados.items())
print(items.sort(key=lambda x: x[1], reverse=True))

for i, j in dados:
    print(i, "->", j)