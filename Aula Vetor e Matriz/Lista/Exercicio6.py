#Faça um programa que leia um vetor de 5 numeros inteiros, mostrea soma, a multiplicação e os numeros

import math 


vetor= []
num = 0

while num < 5   :
    numero= int(input(f"Digite um valor para a conta, valor de num {num+1}: "))
    num +=1
    vetor.append(numero)

numero= print(f"Todos os numeros são:{vetor}")
soma= print(f"Soma dos valores é igual: {sum(vetor)}")
multiplicação= print(f"Multiplicação dos valores é igual: {math.prod(vetor) }")


