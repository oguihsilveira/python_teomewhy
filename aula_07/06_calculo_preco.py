def calc_imposto(preco:float, tax_imposto_base:float): # Função para calcular o preço com imposto
    """ A função calc_imposto recebe dois números como argumentos, o preço e o imposto, e retorna o preço com o imposto incluído. 
    A função é definida com anotações de tipo para indicar que os argumentos preco e imposto
    """
    return preco * tax_imposto_base

calc_imposto(100, 0.03) # Chama a função calc_imposto com os valores de 100 e 0.03, e imprime o resultado

####################################################################################################
def calc_imposto2(preco2:float, tax_imposto_base2:float, **kwargs): # Função para calcular o preço com imposto
    """ 
    """
    imposto = preco2 * tax_imposto_base2
    for i in kwargs:
        print(i, kwargs[i])
        imposto = preco2 * kwargs[i]
    return imposto

impostos_gerais = {
    "municipio": 0.01, 
    "estadual": 0.005, 
    "nacional": 0.001
    } # Dicionário com os impostos gerais

calc_imposto2(100, 0.03, **impostos_gerais) # Chama a função calc_imposto2 com os valores de 100 e 0.03, e o dicionário de impostos gerais, e imprime o resultado