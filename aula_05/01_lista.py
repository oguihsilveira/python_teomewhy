# Criando uma lista de idades
idades = [28, 42, 43, 35, 39, 28, 38]
print(idades)

# Verificando o tipo da variável
print(type(idades))

# Lista com dados variados (nome, sobrenome, idade, tem filhos, solteiro, renda)
gui = ["Gui", "Silveira", 20, False, "solteiro", 1000.00]
# Acessando o primeiro elemento ("Téo")
print(gui)

# Tipo da variável gui (lista)
print(type(gui))

# Acessando o terceiro elemento (idade: 32)
print(gui[2])

# Acessando o último elemento usando índice negativo
print(gui[-1])

# Soma das idades
soma_idades = sum(idades) # Com variável
print("Soma das idades: ", soma_idades)

# Soma das idades
print("Soma das idades: ", sum(idades)) # Com função sum() para somar os elementos da lista

# Quantidade de idades
print("Quantidade de idades: ", len(idades)) # Com função len() para contar o número de elementos da lista

# Média das idades
print("Média das idades: ", sum(idades) / len(idades)) # Faz a soma das idade e divide pelo número de elementos da lista (quantidade de idades)

# Menor idade
print("Menor idade: ", min(idades)) # Com função min() para encontrar o menor valor da lista

# Maior idade
print("Maior idade: ", max(idades)) # Com função max() para encontrar o maior valor da lista

# Listas dentro de listas
teo = ["Teo", "Calvo", 20, True, "casado", ["Ana", "Maria", "Claudia"]]
print(teo)

print("Lista: ", teo[5]) # Acessando a lista de filhos
print("Primeiro filho: ", teo[5][0]) # Acessando o primeiro filho (Ana)
print("Tipo de lista: ", type(teo[5])) # Verificando o tipo da lista de filhos (lista)


tamanho = len(teo)
pos = tamanho - 1
print("Último elemento: ", teo[pos]) # Acessando o último elemento da lista

filhos = teo[pos] # Acessando a lista de filhos

teo[pos][len(filhos) - 1] # Acessando o último filho da lista de filhos (Claudia) usando o tamanho da lista de filhos para calcular o índice do último elemento

teo[-1] # Acessando o último elemento da lista usando índice negativo (filhos)
teo[-1][-1] # Acessando o último filho da lista de filhos usando índices negativos (Claudia)
teo[-1][-2] # Acessando o penúltimo filho da lista de filhos usando índices negativos (Maria)

teo[0-4] # Acessando os primeiros 4 elementos da lista (nome, sobrenome, idade, tem filhos)
teo[0:4] # Acessando os primeiros 4 elementos da lista usando slicing (nome, sobrenome, idade, tem filhos)

teo[4][3:5] # Acessando os últimos 2 elementos da lista de filhos usando slicing (Maria, Claudia)
teo[4][-2:] # Acessando os últimos 2 elementos da lista de filhos usando índices negativos e slicing (Maria, Claudia)

joao = ["Joãozinho", "Silveira", 20, False, "solteiro", ["Ana", "Maria", "Claudia"], [1500.00, 2000.00, 2500.00]]
salarios = joao[-1]
print("Salários: ", salarios) # Acessando a lista de salários
print("Salário mais recente: ", salarios[-1]) # Acessando o salário mais recente usando índice negativo
salarios[::-1] # Acessando a lista de salários em ordem reversa usando slicing com passo negativo