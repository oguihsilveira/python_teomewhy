def par_impar(numero:int): # Função para verificar se um número é par ou ímpar
    if numero % 2 == 0: # Verifica se o número é divisível por 2, ou seja, se é par
        return "Par" # Retorna a string "Par" se o número for par
    else:
        return "Ímpar" # Retorna a string "Ímpar" se o número for ímpar

numero = int(input("Digite um número: "))

par_impar(numero) # Chama a função par_impar com o número digitado pelo usuário para verificar se é par ou ímpar

resultado = par_impar(numero) # Armazena o resultado da função par_impar em uma variável, embora a função não retorne nenhum valor