#Faça um programa que peça as quatro notas de seis alunos, calcule e armazene num vetor a media de cada aluno, 
# imprima o numero de alunos com media maior ou igual a 7

print("Preencha as notas fos alunos ")
matriz= []

for i in range(2):
    linha= []
    for coluna in range(2):
        nota= int(input("Digite a nota do aluno: ")) #Pede a nota dos alunos
        linha.append(nota) #adiciona nota de cada aluno
    matriz.append(linha) #cria linha e colunas

print(f"Tabela das notas dos alunos: /n {matriz} ")
print()
print()
    
