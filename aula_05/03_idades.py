""" idades = [17, 32, 41, 54]
print(idades) # Imprimindo a lista de idades

idades.append(28) # Adicionando um elemento no final da lista
print(idades) # Imprimindo a lista de idades após adicionar o elemento 28
 """
idades = []

while True:
    idade = input("Digite uma idade: ")
    
    if idade == "":
        break
    idades.append(int(idade)) # Adicionando a idade digitada na lista de idades

    print("Lista de idades: ",idades) # Imprimindo a lista de idades após adicionar a nova idade

    media = sum(idades) / len(idades) # Calculando a média das idades
    minimo = min(idades) # Encontrando a menor idade
    maximo = max(idades) # Encontrando a maior idade
    qntde = len(idades) # Contando a quantidade de idades

    print("Média das idades: ", media) # Imprimindo a média das idades
    print("Menor idade: ", minimo) # Imprimindo a menor idade
    print("Maior idade: ", maximo) # Imprimindo a maior idade
    print("Quantidade de idades: ", qntde) # Imprimindo a quantidade de idades