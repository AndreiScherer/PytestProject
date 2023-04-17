import cryptographyFramework

def validar_usuario(usuario):
    if len(usuario) > 0 and len(usuario) <= 30 and usuario[0].isupper() and usuario.isalnum():
        return True
    else:
        print("Usuário inválido! O usuário deve ter a primeira letra maiúscula, sem caracteres especiais e sem espaços e no máximo 30 caracteres.")
        return False

def validar_senha(senha):
    if len(senha) >= 10 and any(char.isdigit() for char in senha) and any(char.isupper() for char in senha) and any(char.islower() for char in senha) and any(char in "!@#$%^&*()_+-=[]{}|;:,.<>?/" for char in senha):
        return True
    else:
        return False

def validar_mensagem(usuario, senha, mensagem):   
    if len(mensagem) <= 70:
        texto_encriptado = cryptographyFramework.encryptMessage(usuario, senha, mensagem)
        cryptographyFramework.saveNewLine(texto_encriptado)
        return True
    else:
        print("Mensagem inválida! A mensagem deve ter no máximo 70 caracteres.")
        return False