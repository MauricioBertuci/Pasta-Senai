#Faça um programa que peça uma nota entre 0 a 10. mostre uma mensagem caso o valor seja invalido e continue pedindo até que o user informe um valido 

nota= float(input("Digite sua nota: "))

while nota > 10 or nota < 0:
    print("Valor invalido")
    nota= float(input("Digite sua nota: "))
else:
    print("Bouaaa !!")

    
