#Crie um programa que dado o valor, a taxa e o tempo, efetuar o cálculo do valor de uma prestação em atraso, utilizando a fórmula:
#prestação = valor + (valor * (taxa/100) * tempo)

print('--'*30)
print("PRESTAÇÂO DE ATRASO")
print('--'*30)
print('\n')

valor= float(input("Valor da divida: ")) 
tempo= int(input('Tempo para quitar a divida em meses: '))
#taxa= float(input('Taxa ao mes : '))
#prestação= print(valor*(valor*(taxa/100)*tempo))

if tempo <= 3:
    taxa= 1
else:
    taxa= 15

prestação=(valor*(valor*(taxa/100)*tempo))
print(f'A prestação fica em {prestação:.2f}')