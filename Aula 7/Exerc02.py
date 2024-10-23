# Capturando exceções múltiplas: Crie um programa que peça ao usuário o 
# nome de uma cor e mostre seu valor em RGB de acordo com um dicionário 
# pré-definido. O programa deve tratar exceções caso o nome da cor não exista 
# no dicionário. 


def cores():
    cores = {'vermelho': (255, 0, 0), 'verde':(0, 255, 0), 'azul': (0, 0, 255)}
    try:
        cor = input('Digite o nome de uma cor: ').lower()
        if cor in cores:
            print(f'O valor de {cor} em RGB é {cores[cor]}')
        else:
            print('Cor não encontrada')
            
    except KeyError:
        print('Cor não encontrada')

cores()