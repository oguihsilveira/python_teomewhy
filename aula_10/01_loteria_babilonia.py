""" numero_sorteio = 7  # Número que o usuário deve adivinhar

while True:  # Executa o bloco repetidamente até que seja interrompido por um break
    numero_usuario = int(input("Entre com um número: "))  # Solicita um número ao usuário

    if numero_sorteio == numero_usuario:  # Verifica se o usuário acertou o número
        print("Parabéns, você ganhou!")  # Exibe mensagem de sucesso
        break  # Encerra o laço

    elif numero_usuario > numero_sorteio:  # Verifica se o número informado é maior que o sorteado
        print("Número muito alto. Tente um número menor.")  # Orienta o usuário a tentar um número menor

    elif numero_usuario < numero_sorteio:  # Verifica se o número informado é menor que o sorteado
        print("Número muito baixo. Tente um número maior.")  # Orienta o usuário a tentar um número maior

    else:  # Caso nenhuma condição anterior seja atendida
        pass  # Não executa nenhuma ação """

####################################################################################################

""" for i in range(3):  # Permite no máximo 3 tentativas
    numero_usuario = int(input("Entre com um número: "))  # Solicita um número ao usuário

    if numero_sorteio == numero_usuario:  # Verifica se o usuário acertou o número
        print("Parabéns, você ganhou!")  # Exibe mensagem de sucesso
        break  # Encerra o laço antes das 3 tentativas

    elif numero_usuario > numero_sorteio:  # Verifica se o número informado é maior que o sorteado
        print("Número muito alto. Tente um número menor.")  # Orienta o usuário a tentar um número menor

    elif numero_usuario < numero_sorteio:  # Verifica se o número informado é menor que o sorteado
        print("Número muito baixo. Tente um número maior.")  # Orienta o usuário a tentar um número maior

    else:  # Caso nenhuma condição anterior seja atendida
        pass  # Não executa nenhuma ação """

####################################################################################################

import random

def get_input():
    while True:  # Executa o bloco repetidamente até que seja interrompido por um break
        try:
            numero_usuario = int(input("Entre com um número: "))  # Solicita um número ao usuário
    
        except ValueError as erro:
            print("Valor inválido!")
            continue

        if 1 <= numero_usuario <= 15:
            return numero_usuario
        
        print("Valor inválido! O valor deve ser entre 1 e 15.")


def check_numbers(sorteio, usuario):
    if numero_sorteio == numero_usuario:  # Verifica se o usuário acertou o número
        print("Parabéns, você ganhou!")  # Exibe mensagem de sucesso
        return True

    elif numero_usuario > numero_sorteio:  # Verifica se o número informado é maior que o sorteado
        print("Número muito alto. Tente um número menor.")  # Orienta o usuário a tentar um número menor
        return False

    elif numero_usuario < numero_sorteio:  # Verifica se o número informado é menor que o sorteado
        print("Número muito baixo. Tente um número maior.")  # Orienta o usuário a tentar um número maior
        return False

    else:  # Caso nenhuma condição anterior seja atendida
        return False

numero_sorteio = random.randint(1,15)

for i in range(3):  # Permite no máximo 3 tentativas
    
    numero_usuario = get_input()

    if check_numbers(sorteio=numero_sorteio, usuario=numero_usuario):
        break