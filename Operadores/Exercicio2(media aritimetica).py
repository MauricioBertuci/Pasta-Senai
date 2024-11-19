#Dado a nota das provas p1, p2 e p3, calcular a media aritimetica das notas 

P1= float(input('Digite a NOTA: '))
P2= float(input('Digite a NOTA: '))
P3= float(input('Digite a NOTA: '))
media= (P1 + P2 + P3)/3
print(f'A media dos alunos é {media}') #usado para aparecer todas as casas
print(f'A media dos alunos é {media:.2f}') #usado para aparecer apenas duas casas decimais
