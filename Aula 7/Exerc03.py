# Bloco else e finally: Escreva um programa que solicite um número ao 
# usuário. Se o número for maior que 10, exiba uma mensagem dizendo que o 
# número é válido. Utilize o bloco else para imprimir que o programa foi 
# executado com sucesso, e o bloco finally para imprimir "Programa 
# encerrado". 


def verificar_num():
    try:
        num = int(input("Digite um número: "))
        if num > 10:
            print("O número é válido")

    except ValueError:
        print("Erro: O valor digitado não é um número")
    else:
        print("Programa executado com sucesso")
        
    finally:
        print("Programa encerrado")

verificar_num()