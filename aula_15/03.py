tipo = input("Entre com o tipo: [Casquinha (R$ 4,99) / Milkshake (R$ 6,99) / Pote (R$ 11,99)] ")
tipo = tipo.lower()

sabor = input("Escolha o sabor: [Morango / Creme / Chocolate] ")
sabor = sabor.lower()

cobertura = input("Escolha a cobertura: [Caramelo (R$ 1,99) / Morango (R$ 1,99) / Chocolate (R$ 1,99) / Sem cobertura (R$ 0,00)] ")
cobertura = cobertura.lower()

while True:
    valor = 0
    if (tipo == "casquinha"):
        valor += 4.99
        break

    elif (tipo == "milkshake"):
        valor += 6.99
        break

    elif (tipo == "pote"):
        valor += 11.99
        break

    else:
        print("Entre com um valor válido.")

if cobertura in ["caramelo", "morango", "chocolate"]:
    valor += 1.5

txt = f"Seu sorvete {tipo} de {sabor} com cobertura de {cobertura} custou R${valor:.2f}"
print(txt)