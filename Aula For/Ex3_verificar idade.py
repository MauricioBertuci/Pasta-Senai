#Faça um programa que peça N pessoas a sua idade, ao final o program devera verificar se a media de idade da turma 
#varia entre 0 25,26 e 60 e amior que 60, e então, dizer se a turma é jovem,adulta ou idosa  

# Forma1
qtd_pessoas= int(input("Digite a quantidade de pessoas da turma: "))
soma= 0 

for i in range(1,qtd_pessoas+1):
    idade= int(input(f"Digite a idade da pessoas {i}: "))
    soma += idade
    media = soma/qtd_pessoas
print(media)

if media >= 0 and media <= 25:
        print("Turma de Jovens")
elif media >= 26 and media <= 60:
        print("Turma de Adultos")
else:
        print("Turma de Idosos")