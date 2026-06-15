# Listas e Tuplas em Python
dados_ana = [23, 1, 1.65, "Ana", "Feminino"] # Lista de dados sobre Ana
print(dados_ana) # Imprime a lista completa de dados sobre Ana

dados_ana.append("Engenheira") # Adiciona a profissão "Engenheira" à lista de dados sobre Ana
print(dados_ana) # Imprime a lista atualizada de dados sobre Ana

# Tuplas são semelhantes às listas, mas são imutáveis, o que significa que não podemos modificar os itens após a criação da tupla. Elas são definidas usando parênteses () em vez de colchetes [].
tupla_ana = (23, 1, 1.65, "Ana", "Feminino", [1500, 1600, 1700]) # Tupla de dados sobre Ana com uma lista de números como um dos elementos
print(tupla_ana) # Imprime a tupla completa de dados sobre Ana

tupla_ana[5].append(1800) # Adiciona o número 1800 à lista que é o sexto elemento da tupla
print(tupla_ana) # Imprime a tupla atualizada de dados sobre Ana, mostrando a lista modificada dentro da tupla