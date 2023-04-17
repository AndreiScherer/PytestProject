from valida_login import *

while True:
    user = input('Digite o user: ')
    if validar_usuario(user):
            break
while True:
    senha = input('Digite a senha: ')
    if validar_senha(senha):
            break
while True:
    mensagem = input('Digite a mensagem: ') 
    if validar_mensagem(user, senha, mensagem):
        break
    else:
        print("Mensagem inválida! Tente novamente.")