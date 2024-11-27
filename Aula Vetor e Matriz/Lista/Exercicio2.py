#Faça um programa que leia um vetor de 10 numeros reias e mostre-os

valor = []
num = 0 
while num < 10:
    valor.append(float(input("Digite um numero: ")))
    num +=1
valor.reverse()
print(valor)