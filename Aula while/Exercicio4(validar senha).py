#crie um programa que solicite a senha de um user e depois, peça pra digitar novamente até que as duas senhas sejam correspondestes

import time

senha1 = input("Digite sua senha: ")
senha2 = input("Digite sua senha: ")
contador = 0
erro = 0

while senha1 != senha2:
    print("Senha errada, digite novamente.")
    senha1 = input("Digite sua novamente: ")
    senha2 = input("Digite sua novamente: ")
    erro += 1
    if senha1 == senha2:
        print("Bouaaa !!")
        break
    if erro == 3:
        print("Espere 5 segundos para colocar a senha. ")
        time.sleep(5)
    if erro == 5:
        print("Errou 5 vezes sua conta está suspensa, ligue para central !")
        print("(11) 9874-2131")
        break
        
