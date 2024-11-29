#Faça um programa que peça as quatro notas de seis alunos, calcule e armazene num vetor a media de cada aluno, 
# imprima o numero de alunos com media maior ou igual a 7

#Pedindo notas
print("Preencha as notas fos alunos ")
matriz= []
for aluno in range(2):
    aluno= input("Digite o nome do aluno: ")
    # nome = [] #verificarr
    linha= []
    for coluna in range(2):
        valor= float(input(f"Digite a nota {coluna+1} do aluno {aluno}: ")) 
        linha.append(valor) 
    matriz.append(linha) 


print(f"Tabela das notas dos alunos:  {matriz} ")

#caucular media
medias_aluno = []
for linha in matriz:
    media = sum(linha) / len(linha)
    # nome.append(aluno) ##verificarrrrrrr
    medias_aluno.append(media) 
print(f"Media dos alunos: {medias_aluno}") 

#Ver notas
for media in medias_aluno:
    if media >= 7:
        print(f"O aluno Passou !!")
    else:
        print(f"O aluno Reprovou !!")
