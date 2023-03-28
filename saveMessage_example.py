from cryptographyFramework import *

initializeWrite()
user = "Andrei"
password = "@Als1234"
encryptedText = encryptMessage(user, password, "Minha mensagem misteriosa!")
saveNewLine(encryptedText)
encryptedText = encryptMessage(user, password, "Minha segunda mensagem misteriosa!")
saveNewLine(encryptedText)

