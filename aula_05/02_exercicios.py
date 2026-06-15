lista = [1,2,2,2,3,3,4,5,5,5,5,5,6,7,8,8,8,8,9,9,10]

numero = int(input("Digite um número: "))

contador = 0
""" for i in lista: # Percorre cada elemento da lista e imprime o valor
    print(i) """

for i in lista: # Percorre cada elemento da lista e verifica se é igual ao número digitado
    if i == numero: # Se o elemento for igual ao número digitado, incrementa o contador
        contador += 1

print("Quantidade de", numero,":", contador) # Imprime a quantidade de vezes que o número digitado aparece na lista