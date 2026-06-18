nome_arquivo = "./aula_09/historia_01.txt"

with open(nome_arquivo, mode="r") as open_file:
    conteudo = open_file.read()

print(conteudo)

""" # Abre arquivo em formato de leitura
open_file = open(nome_arquivo, mode="r")

# Lê os dados do arquivo
conteudo = open_file.read() # Fecha o arquivo
open_file.close()

print(conteudo) """