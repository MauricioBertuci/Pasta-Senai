
print("--"*30)
print("ESCOLHAS: ")
print("--"*30)
print("papel")
print("tesoura")
print("pedra")
print("--"*30)

p1=input("Escolha do jogador 1 foi : ")
p2=input("Escolha do jogador 2 foi: ")

#PRIMERIA OPÇÃO DE CODIGO
#empates
if p1 == "tesousa" and p2 == "tesoura":
    print("Empate entre os jodadores !!")
elif p1 == "pedra" and p2 == "pedra":
    print("Empate entre os jodadores !!")
elif p1 == "papel" and p2 == "papel":
    print("Empate entre os jodadores !!")

#jogador 2 ganha
elif p1 == "tesoura" and p2 == "pedra":
    print("O jogador 2 ganhou !!")
elif p1 == "papel" and p2 == "tesoura":
    print("O jogador 2 ganhou !! ")
elif p1 == "papel" and p2 == "pedra":
    print("O jogador 1 ganhou !! ")

#jogador 1 ganha 
elif p2 == "tesoura" and p1 == "pedra":
    print("O jogador 1 ganhou !!")
elif p2 == "papel" and p1 == "tesoura":
    print("O jogador 1 ganhou !!")
elif p2 == "papel" and p1 == "pedra":
    print("O jogador 2 ganhou !! ")


#SEGUNDA OPÇÃOD DE CODIGO
if p1 == p2:
    print("EMPATE !!")    
elif (p1 == "pedra" and p2 == "tesoura") or (p1 == "tesoura" and p2 == "papel") or p1 == "papel" and p2 == "pedra":
    print("jogador 1 ganha !!")
elif (p1 == "tesoura" and p2 == "pedra") or (p1 == "papel" and p2 == "tesoura") or p1 == "pedra" and p2 == "papel":
    print("jogador 2 ganha !!")
else:
    print("Palavra invalida !!")


