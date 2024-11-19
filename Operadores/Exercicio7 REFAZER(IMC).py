#Elaborar um programa em Python que cadastre os dados pessoais como (Nome, Sobrenome, Idade, Cidade, Altura, Peso, IMC) solicite os dados de 
#estatura (em metros) e peso (em Kg) de uma pessoa e calcule/visualize seu IMC (Índice de Massa Corporal).

print("\n") #pular linha
#nome= input('Digite seu nome: ')
#sobrenome= input('Digite seu sobrenome: ')
#idade= int(input('Digite seu idade: '))
altura= float(input('Digite sua altura em metro: '))
peso= float(input('Digite seu peso: '))
#cidade= input("Digite sua cidade: ")
div= (peso/altura**2)
print("--"*30)

imc= print(f'Seu IMC é {div:.2f}')
print('\n')

if imc <= 16.9:
    print('De acordo com seu IMC voce está: MUITO BAIXO DO PESO')
elif imc >= 17 and 18.4:
    print('De acordo com seu IMC voce está: ABAIXO DO PESO')
elif imc >= 18.5 and 24.9:
    print('De acordo com seu IMC voce está: SAUDAVEL')
elif imc >= 25 and 29.9:
    print('De acordo com seu IMC voce está: SOBREPESO')
elif imc >= 30 and 34.9:
    print('De acordo com seu IMC voce está: OBESO I')
elif imc >= 34 and 39.9:
    print('De acordo com seu IMC voce está: OBESO II')
else:
    print('De acordo com seu IMC voce está: OBESO III')
