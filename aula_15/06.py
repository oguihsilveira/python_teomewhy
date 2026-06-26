items = "laranja cereja miojo carvão picanha"
print(items)

escolha = input("Escolha um item: ")
escolha.lower()

if (escolha in items):
    print("Seu item escolhido existe.")

else:
    print("Seu item escolhido não existe, escolha um item válido.")