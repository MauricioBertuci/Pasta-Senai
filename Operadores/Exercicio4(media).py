#Faça um programa que cadastre (nome,sobrenome,idade,ra) peça as  notas bimestrais e mostre a media

print(input('Digite seu nome: '))
print('\n')
print(input('Digite seu sobrenome: '))
print('\n')
print(input('Digite seu idade: '))
print('\n')
print(input('Digite seu Ra: '))
print('\n')
print('AGORA DIGITE SUAS NOTAS')
print('\n')
nota1=float(input('Digite sua nota do bimestre: '))
nota2=float(input('Digite sua nota do bimestre: '))
nota3=float(input('Digite sua nota do bimestre: '))
nota4=float(input('Digite sua nota do bimestre: '))
media=(nota1+nota2+nota3+nota4)/4
print(f'MEDIA DAS NOTAS É {media:.2}')
print('\n')