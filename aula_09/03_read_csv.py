arquivo = "./aula_09/data.csv"  # Caminho do arquivo CSV

with open(arquivo) as open_file:  # Abrindo o arquivo para leitura
    lines = open_file.readlines()  # Lendo todas as linhas do arquivo e armazenando em uma lista

print(lines)  # Exibindo a lista completa de linhas lidas do arquivo

for l in lines:  # Percorrendo cada linha da lista
    print(l)  # Exibindo uma linha por vez

dados = dict()  # Criando um dicionário vazio

chaves = lines[0].strip("\n").split(";")  # Obtendo o cabeçalho, removendo a quebra de linha e separando as colunas pelo ";"

for c in chaves:  # Percorrendo cada coluna encontrada no cabeçalho
    dados[c] = []  # Criando uma chave no dicionário com uma lista vazia para armazenar os valores da coluna

for l in lines[1:]:  # Percorrendo as linhas de dados, ignorando a primeira linha (cabeçalho)
    
    valores = l.strip("\n").split(";")
    
    for i in range(0, len(valores)):
        dados[chaves[i]].append(valores[i])

idades = []
for i in dados["idade"]:
    idades.append(int(i))

media = sum(idades) / len(idades)