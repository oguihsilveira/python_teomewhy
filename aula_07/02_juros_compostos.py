def juros_compostos(aporte:int, taxa:float, anos:int) -> float: # Função para calcular o valor futuro de um investimento usando juros compostos
    """ Juros compostos servem para calcular o valor futuro de um investimento, levando em consideração os juros acumulados ao longo do tempo. 
    A fórmula é: VF = P * (1 + r) ** n, onde P é o aporte inicial, r é a taxa de juros e n é o número de períodos.
    Aporte: O valor inicial investido.
    Taxa: A taxa de juros anual (em decimal, por exemplo, 0.13 para 13%).
    Anos: O número de anos que o dinheiro ficará investido.
    """
    return aporte * (1 + taxa) ** anos

# juros_compostos(1000, 0.13, 10) # Calcula o valor futuro de um investimento de 1000 com uma taxa de 5% ao ano por 10 anos
juros_compostos(aporte=1000, taxa=0.13, anos=10) # Calcula o valor futuro de um investimento de 1000 com uma taxa de 5% ao ano por 10 anos, usando argumentos nomeados

