texto = """
escolha a sua água para comprar:
1 - água mineral natural (R$ 1,50)
2 - água mineral com gás (R$ 2,50)
"""

opcao = input(texto)
valor_item = 0

if opcao == "1":
    valor_item = 1.50
elif opcao == "2":
    valor_item = 2.50

if valor_item == 0:
    print("entre com a opção correta por favor")
else:
    print("sua conta é", valor_item)