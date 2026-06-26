
tipo = input("Escolha a sua água para comprar:\n(1) Água mineral natural\n(2) Água mineral com gás")

valor = 0
qntde = int(input("Digite a quantidade de garrafas que deseja comprar: "))

if tipo == "1":
    valor = 1.5 * qntde
    print(f"Valor: R$ {valor}")
elif tipo == "2":
    valor = 2.5 * qntde
    print(f"Valor: R$ {valor}")
else:
    print("Entre com um valor válido.")