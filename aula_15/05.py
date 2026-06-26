nome = input("Insira seu nome: ")
nome_split = nome.lower().split(" ")

if 'machado' in nome_split: #Guiljerme Machado -> ["guilherme", "machado"]
    print("Essa pessoa é Machado.")

if 'silveira' in nome_split: #Guiljerme Machado -> ["guilherme", "silveira"]
    print("Essa pessoa é Silveira.")

if 'machado' not in nome_split and 'silveira' not in nome_split:
    print("Essa pessoa não é Machado, nem Silveira.")