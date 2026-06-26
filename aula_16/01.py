palavra = input("Entre com a palavra: ").lower()

count = 0

for letra in palavra:
    if letra == "a":
        count += 1

print(f"A palavra {palavra} tem {count} letras 'a'.")

