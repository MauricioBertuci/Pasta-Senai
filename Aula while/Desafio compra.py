#Crie um programa em linguagem Python que permite ao usuário inserir os
#valores dos produtos comprados por um cliente.



#input("Digite o valor: ")
cliente=input("Digite seu nome: ")
soma=0
while True:
    valor=  int(input("Digite o valor do produto: "))
    if valor<0:
        print("erro!!")
        int(input("Digite o valor do produto novamente: "))
    elif valor>0: 
        int(input("Digite o valor do produto: "))
    elif valor == 0:
        print(f"Obrigado pela compra {cliente}")
        break
