import requests # Para realizar requisições na web
import json # Para tratar jso de listas/dicionários
from tqdm import tqdm # Barra de progresso no terminal

import pandas as pd

ceps = [
    "88801000",
    "88802150",
    "88804010",
    "88815050",
    "88817600",
    "88701000",
    "88705150",
    "88845000",
    "88870000",
    "88850000",
]

#url = "https://viacep.com.br/ws/19060100/json/"

url = "https://viacep.com.br/ws/{cep}/json/"
dados = []
for i in tqdm(ceps):
    resposta = requests.get(url.format(cep=i))
    if resposta.status_code == 200:
        #resposta.raw()
        #dados = resposta.json()
        dados.append(resposta.json())

#print(dados)
#type(dados)

dataset = pd.DataFrame(dados)
print(dataset)
dataset.to_csv("./aula_11/ceps.csv", sep=";")

with open("./aula_11/ceps.json", "w", encoding='utf-8') as open_file:
    json.dump(dados, open_file, ensure_ascii=False, indent=4)