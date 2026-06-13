saldo_total = 0

while True:
    saldo = input("entre com o saldo: ")
    print("Seu saldo é: R$", saldo)
    
    if saldo == "": # Se o usuário apenas apertou Enter
        break       # Sai do laço imediatamente