from valida_login import *

def test_valida_user():
    assert validar_usuario("Usuario1") == True
    assert validar_usuario("usuario1") == False
    assert validar_usuario("Usuario1!") == False
    assert validar_usuario("") == False
    assert validar_usuario("UsuarioComMaisDeTrintaCaracteres1234567890") == False

def test_valida_senha():
    assert validar_senha("Senha1234#") == True
    assert validar_senha("senha123#") == False
    assert validar_senha("Senha#") == False
    assert validar_senha("Senha123") == False
    assert validar_senha("SenhaABC#") == False
    assert validar_senha("") == False
    assert validar_senha("Senhacommaisde10caracteressemcaracteresespeciais") == False

def test_valida_mensagem():
    assert validar_mensagem('usuario', 'senha', 'mensagem') == True

def test_valida_mensagem_invalida():
    assert validar_mensagem('usuario', 'senha', 'Uma mensagem com mais de 70 caracteres que deve ser inválida e não ser criptografada.') == False
