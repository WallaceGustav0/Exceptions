# Tratamento de exceções básicas: Escreva um programa que peça ao usuário 
# dois números e faça a divisão do primeiro pelo segundo. Se o usuário inserir 
# um valor inválido ou tentar dividir por zero, o programa deve exibir uma 
# mensagem de erro apropriada. 


def divisao():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        if num2 == 0:
            print("Erro: Não é possível dividir por zero!")
        else:
            print(f"{num1} / {num2} = {num1 / num2}")
            
    except ValueError:
        print("Erro: Valor inválido. Insira um número.")

divisao()