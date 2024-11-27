#Faça um programa que peça as quatro notas de seis alunos, calcule e armazene num vetor a media de cada aluno, 
# imprima o numero de alunos com media maior ou igual a 7

print("Preencha as notas fos alunos ")
notas_matriz= []

#pedir nome do aluno e digitar a nota dele 

#Pedindo as notas dos alunos
for aluno in range(2):
    linha= []
    print(f"Notas do aluno {aluno+1}")
    for coluna in range(2):
        valor_nota= int(input(f"{coluna+1}° nota: ")) #Pede a nota dos alunos
        linha.append(valor_nota) #adiciona nota de cada aluno em linha 
    notas_matriz.append(linha) #add linhas na matriz
print(f"Tabela das notas dos alunos: /n {notas_matriz} ")

#Media dos alunos
medias = []
for linha in notas_matriz:
    media = sum(linha)/len(linha)   





    
