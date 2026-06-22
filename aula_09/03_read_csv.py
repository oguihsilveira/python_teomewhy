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

    valores = l.strip("\n").split(";")  # Removendo a quebra de linha e separando os valores da linha pelo ";"

    for i in range(0, len(valores)):  # Percorrendo os índices dos valores encontrados na linha
        dados[chaves[i]].append(valores[i])  # Adicionando cada valor na lista correspondente à sua coluna

idades = []  # Criando uma lista vazia para armazenar as idades como números inteiros

for i in dados["idade"]:  # Percorrendo todas as idades armazenadas no dicionário
    idades.append(int(i))  # Convertendo a idade de texto para inteiro e adicionando na lista

media = sum(idades) / len(idades)  # Calculando a média das idades