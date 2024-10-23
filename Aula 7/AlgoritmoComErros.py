def calcular_media(notas):
    if len(notas) == 0:
        raise ZeroDivisionError('Não tem notas para calcular a média')
    soma = sum(notas)
    media = soma / len(notas)
    return media


def exibir_media(notas):
    try:
        media = calcular_media(notas)
        if media > 7:
            print(f"Parabéns! Sua média é {media:.2f} e você foi aprovado.")
        else:
            print(f"Sua média é {media:.2f} e infelizmente, você não foi aprovado.")
    except ZeroDivisionError as e:
        print(f"Erro: {e}")


# Programa principal
try:
    numero_notas = int(input("Quantas notas você vai inserir? "))
    if numero_notas <= 0:
        raise ValueError("Insira um número de notas maior que zero")
        
    notas = []
    
    for i in range(numero_notas):
        nota = float(input(f"Digite a nota {i + 1}: "))
        notas.append(nota)
    
    exibir_media(notas)

except ValueError as e:
    print(f"Erro: {e}")

finally:
    print("Programa finalizado.")