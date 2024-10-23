# Simulação de transações: Crie um programa que simule uma transferência 
# bancária. Peça ao usuário o saldo da conta e o valor da transferência. Caso o 
# saldo seja insuficiente, levante uma exceção do tipo ValueError com a 
# mensagem "Saldo insuficiente". Trate a exceção adequadamente e informe o 
# usuário. 


def simula_transferencia():
    try:
        saldo = float(input("Digite o saldo da conta: "))
        tranferencia = float(input("Digite o valor da tranferencia: "))
        if tranferencia > saldo:
            raise ValueError("Saldo insuficiente")
        saldo -= tranferencia
        
        print(f"Saldo atual: R$ {saldo:.2f}")
  
    except ValueError as e:
        print(f"Erro: {e}")

simula_transferencia()