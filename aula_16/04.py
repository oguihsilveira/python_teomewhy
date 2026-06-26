soma = 0

while True:
    entrada = input("Entre com um valor: ")
    if entrada == "":
        break

    soma += float(entrada)

print(f"A soma total dos valores é R${soma:.2f}")