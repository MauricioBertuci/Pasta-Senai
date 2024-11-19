#Numa eleição existem três candidatos:
#Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final
#mostrar o número de votos de cada candidato.
#mostre quem foi o mais votado

print("--"*30)
print("Numero do Canditado Chupeta: 10")
print("Numero do Canditado Porpeta de Galinha: 20")
print("Numero do Canditado Vida Mais Pobre: 30")
print("--"*30)

qnt_pessoas= int(input("Quantas pessoas irão votar: "))
Chuepeta = 0
Porpeta = 0
Pobre = 0
conciente = 0

for i in range(1,qnt_pessoas+1):
    voto= input("Digite seu numero voto: ")
    if voto == "10":
        Chuepeta += 1
    elif voto == "20":
        Porpeta += 1
    elif voto == "30":
        Pobre += 1
    else:
        conciente  += 1
        print("Seu voto é nulo")

print("\n")
print(f"Ao todo o candidato Chupeta teve {Chuepeta} voto")
print(f"Ao todo o candidato Porpeta de Galinha teve {Porpeta} voto")
print(f"Ao todo o candidato Vida Mais Pobre teve {Pobre} voto")
print(f"Ao todo tiveram {conciente} votos concientes")

if Chuepeta>Porpeta and Chuepeta>Pobre and Chuepeta>conciente:
    print("1° - Chupeta ")

elif contagem_Porpeta > contagem_Chuepeta and contagem_Porpeta > contagem_Pobre and contagem_Porpeta > contagem_conciente:
    print("1°")