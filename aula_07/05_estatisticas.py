def soma(a:float, b:float) -> float: # Função para somar dois números
    """ A função soma recebe dois números como argumentos e retorna a soma desses números. 
    A função é definida com anotações de tipo para indicar que os argumentos a e b devem ser do tipo float, e que a função retorna um valor do tipo float.
    """
    return a + b

def media(a:float, b:float) -> float: # Função para calcular a média de dois números
    """ A função media recebe dois números como argumentos e retorna a média desses números. 
    A função é definida com anotações de tipo para indicar que os argumentos a e b devem ser do tipo float, e que a função retorna um valor do tipo float.
    """
    return soma(a, b) / 2

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))

print("A soma de A e B é: ", soma(a, b)) # Chama a função soma com os valores de a e b e imprime o resultado
print("A média de A e B é: ", media(a, b)) # Chama a função media com os valores de a e b e imprime o resultado

########################################################################################################################

#funções com três argumentos

def soma2(a2:float, b2:float, c2:float) -> float: # Função para somar três números
    """ A função soma2 recebe três números como argumentos e retorna a soma desses números. 
    A função é definida com anotações de tipo para indicar que os argumentos a, b e c devem ser do tipo float, e que a função retorna um valor do tipo float.
    """
    return a2 + b2 + c2

def media2(a2:float, b2:float, c2:float) -> float: # Função para calcular a média de três números
    """ A função media2 recebe três números como argumentos e retorna a média desses números. 
    A função é definida com anotações de tipo para indicar que os argumentos a, b e c devem ser do tipo float, e que a função retorna um valor do tipo float.
    """
    return soma2(a2, b2, c2) / 3

a2 = float(input("Digite o valor de A: "))
b2 = float(input("Digite o valor de B: "))
c2 = float(input("Digite o valor de C: "))

########################################################################################################################

def soma3(a3:float, b3:float, c3=0) -> float: # Função para somar três números com um argumento opcional
    """ A função soma3 recebe três números como argumentos, sendo o terceiro argumento opcional com um valor padrão de 0, e retorna a soma desses números.
    A função é definida com anotações de tipo para indicar que os argumentos a, b e c devem ser do tipo float, e que a função retorna um valor do tipo float."""
    return a3 + b3 + c3

def media3(a3:float, b3:float, c3=0) -> float: # Função para calcular a média de três números com um argumento opcional
    """ A função media3 recebe três números como argumentos, sendo o terceiro argumento opcional com um valor padrão de 0, e retorna a média desses números.
    A função é definida com anotações de tipo para indicar que os argumentos a, b e c devem ser do tipo float, e que a função retorna um valor do tipo float."""
    return soma3(a3, b3, c3) / 3

a3 = float(input("Digite o valor de A: "))
b3 = float(input("Digite o valor de B: "))
c3 = float(input("Digite o valor de C: "))

print(soma3(a3, b3)) # Chama a função soma3 com os valores de a3 e b3, pois o argumento c3 é opcional e tem um valor padrão de 0, e imprime o resultado
print(media3(a3, b3)) # Chama a função media3 com os valores de a3 e b3, pois o argumento c3 é opcional e tem um valor padrão de 0, e imprime o resultado

########################################################################################################################

def soma4(a4:float, b4:float, *args) -> float: # Função para somar três números com um argumento opcional
    valores = [a4, b4] + list(args) # Cria uma lista com os valores de a4, b4 e os argumentos adicionais passados para a função
    return sum(valores) # Retorna a soma de todos os valores na lista usando a

def media4(a4:float, b4:float, *args) -> float: # Função para calcular a média de três números com um argumento opcional
    return soma4(a4, b4, *args) / (len(args)+2) # Retorna a média de todos os valores usando a função soma4 para calcular a soma e dividindo pelo número total de valores, que é o número de argumentos adicionais mais 2 (a4 e b4)

a4 = float(input("Digite o valor de A: "))
b4 = float(input("Digite o valor de B: "))
c4 = float(input("Digite o valor de C: "))

print(soma4(a4, b4)) # Chama a função soma4 com os valores de a4 e b4, pois o argumento c4 é opcional e tem um valor padrão de 0, e imprime o resultado
print(media4(a4, b4)) # Chama a função media4 com os valores de a4 e b4, pois o argumento c4 é opcional e tem um valor padrão de 0, e imprime o resultado