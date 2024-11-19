#Faça um programa que peça dois numeros ao usuario e mostre qual o maior e o menor 

valor1= float(input('Digite um valor: '))
valor2= float(input('Digite outro valor: '))

if valor1>valor2:
    print(f'{valor1} é maior que {valor2}')

elif valor2>valor1:
   print(f'{valor2} é maior que {valor1}')

else:
    print(f'{valor1} é igual a {valor2}')


