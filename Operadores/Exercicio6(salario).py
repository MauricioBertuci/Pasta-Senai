#faça um programa que controla dados iniciais (NOME, SOBRENOME, IDADE). depois que perguntar quanto vc ganha por hora e numero de horas de trabalho por mes.
#Caucule e mostre seu salario do mes

print("\n") #pular linha
nome= input('Digite seu nome: ')
sobrenome= input('Digite seu spbrenome: ')
idade= input('Digite seu idade: ')
print('--'*30) #linha para separar
print("\n") #pular linha

hora= int(input('Digite o valor por hora recebido: '))
numerohora= int(input('Digite número de horas trabalhadas no mes: '))
print('--'*30) #linha para separar
print("\n") #pular linha

total= print(f"O salario total do mes é de {hora*numerohora} reais por mes")
totaldolar= hora*numerohora*5
totaldolar= print(f'O salario em dolar total dolar mes é de {totaldolar} dolares por mes')