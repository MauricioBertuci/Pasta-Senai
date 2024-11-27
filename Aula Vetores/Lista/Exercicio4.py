#Faça um programa que leia um vetor de 10 caracteres, diga quantas 
#consoantes foram lidas. Imprima as consoantes 

vetor= [] #ok
consoantes= [] #
num = 0
total_consoantes = 0

while num < 10:
    letra = input(f"Digite numero  {num+1} caracteres, sendo um de cada vez: ").lower()
      
    if letra != "a" and letra != "e" and letra != "i" and letra != "o" and letra != "u":
        total_consoantes +=1
        num +=1
        consoantes.append(letra)

    else:
        vetor.append(letra)
        num +=1 
        
print(F"Total de condosantes {total_consoantes}").sort()
print(f"Todas as consoantes {consoantes}")


