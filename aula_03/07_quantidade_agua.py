texto = """
escolha a sua água para comprar:
1 - água mineral natural
2 - água mineral com gás
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
    quantidade = input("Quantas garrafas?")
    quantidade = int(quantidade) # Conversão necessária para cálculo [18]
    valor_total = valor_item * quantidade
    print("sua conta deu", valor_total)