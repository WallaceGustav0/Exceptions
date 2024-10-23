# Exceções personalizadas: Escreva uma função que verifica se uma senha 
# possui no mínimo 8 caracteres e pelo menos um número. Se a senha não 
# atender aos requisitos, levante uma exceção com uma mensagem 
# personalizada. Trate a exceção e mostre a mensagem ao usuário.


def verificar_senha(senha):
    if len(senha) < 8:
        raise ValueError("A senha deve ter pelo menos 8 caracteres.")
    if not any(char.isdigit() for char in senha):
        raise ValueError("A senha deve ter pelo menos um número.")
    
try:
    senha = input("Digite sua senha: ")
    verificar_senha(senha)
    print("Senha Válida")

except ValueError as e:
    print(f"Erro: {e}")