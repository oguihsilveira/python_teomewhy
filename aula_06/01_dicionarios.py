# Dicionarios são pares de chave-valor, onde cada chave é única e está associada a um valor. Eles são mutáveis, o que significa que podemos adicionar, remover ou modificar os itens após a criação do dicionário.

# Criando um dicionário
alice_dicionario = {
    "nome": "Alice",
    "idade": 24,
    "cidade": "Rio de Janeiro",
    "filhos": ["Bob", "Charlie"], # Lista como valor associado à chave "filhos"
    "casada": False,
    "formacao": ["Psicologia", "Mestrado em Ciência da Computação"], # Lista como valor associado à chave "formacao"
    "cargos":[
        {"nome":"dev jr.", "empresa":"Empresa1"},
        {"nome":"dev pl.", "empresa":"Empresa2"},
        {"nome":"dev sr.", "empresa":"Empresa3"},
    ]
}

print(alice_dicionario["nome"]) # Acessando o valor associado à chave "nome"
print(alice_dicionario["filhos"]) # Acessando o valor associado à chave "filhos"
print(alice_dicionario["formacao"]) # Acessando o valor associado à chave "formacao"

print(alice_dicionario["formacao"][-1]) # Acessando o último item da lista associada à chave "formacao"
print(alice_dicionario["cargos"]) # Acessando o valor associado à chave "cargos"
print(alice_dicionario["cargos"][0]) # Acessando o primeiro item da lista
print(alice_dicionario["cargos"][-1]["nome"]) # Acessando o valor associado à chave "nome" do último dicionário na lista associada à chave "cargos"

alice_dicionario["profissao"] = "Desenvolvedora" # Adicionando um novo par chave-valor ao dicionário
print(alice_dicionario["profissao"]) # Acessando o valor associado à chave "profissao"

print(alice_dicionario.keys()) # Retorna uma lista de todas as chaves do dicionário
print(alice_dicionario.values()) # Retorna uma lista de todos os valores do dicionário

for i in [10,20,30]:
    print(i) # Imprime cada número da lista

for i in alice_dicionario:
    """ print(i) # Imprime cada chave do dicionário """
    print(alice_dicionario[i]) # Imprime o valor associado à chave atual

for chave, valor in alice_dicionario.items():
    print(chave, "->", valor) # Imprime cada chave e seu valor associado no dicionário