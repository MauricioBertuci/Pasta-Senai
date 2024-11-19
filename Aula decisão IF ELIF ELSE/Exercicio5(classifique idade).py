#Elabore um algoritimo que dada a idade de um naador classiffique em uma categoria

print('--'*30)
print("TABELA DE CLASSIFICAÇÃO DE IDADE: ")
infA= print('Infantil A= 5 a 7 anos')
infB= print('Infantil B= 8 a 11 anos')
juvA= print('Juvenil A= 12 a 13 anos ')
juvB= print('Juvenil B= 14 a 17 anos ')
adulto= print('Adultos = Maiores de 18 anos')
print('--'*30)
print('\n')

idade= int(input("Digite sua idade, para verificar sua classificação: "))

if (idade >= 5) and (idade <= 7):
    print('Você é indfantil A')

elif (idade  >=8) and (idade <= 11):
     print('Você é indfantil B')

elif (idade  >=12) and (idade <= 13):
     print('Você é injuvenil A')

elif (idade  >=14) and (idade <= 17):
    print('Você é injuvenil B')

else:
    print('Você é Adulto')