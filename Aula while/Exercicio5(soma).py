#Faça um programa que leia n numeros interios a partir do teclado, até que o user digite 0
#no final mostre a soma de todos os numeros digtados

contador = 0
numero= 15
soma= 0
while numero != 0:
    numero= int(input(f"Digite o numero {contador+1}: "))
    if numero == 0:
        break
    contador += 1
    soma += numero
print(f"A soma dos numeros é de {soma}")
