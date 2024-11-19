#Faça um programa que leia e valide as seguintes informações (e para cada uma
#delas, continue pedindo a informação até o usuário inserir corretamente):
nome= input("Digite seu nome (Deve conte min 3 carateres): ")
idade= int(input("Digite seu nome (maior que 0 e menor que 150): "))
salario=int(input("Digite seu nome (maior do que 0): "))
sexo=input("Digite seu nome (f ou m): ")
estado_civil=input("Digite seu estado civil (s,c,v ou d): ")

while True:
    if idade<=0 and idade>=150:
        int(input("Digite seu nome (maior que 0 e menor que 150): "))