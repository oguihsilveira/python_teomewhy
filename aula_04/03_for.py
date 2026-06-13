soma = 0
quantidade_entradas = 4

for i in range(quantidade_entradas): # Percorre de 0 a 3 (4 iterações)
    altura = float(input("entre com a sua altura: "))
    soma += altura

print("soma das alturas:", soma)