#Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
#Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
#Imprima os três vetores.
par= []
impar= []
vetor = []
num = 0

while num < 20:
    numero = int(input(f"Digite um numero qualquer, rodada {num}: "))
    num +=1
    vetor.append(numero)

    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)


print(f"Todos os valores {vetor}")
print(f"Valores par {par}")
print(f"Valores impar {impar} ")