# Inicializando a matriz de notas com 6 alunos e 4 disciplinas
notas = []

# Lendo as 4 notas de cada um dos 6 alunos
for i in range(6):
    aluno_notas = []
    print(f"Digite as 4 notas do aluno {i+1}:")
    for j in range(4):
        nota = float(input(f"Nota {j+1}: "))
        aluno_notas.append(nota)
    notas.append(aluno_notas)

# Calculando a média de cada aluno e armazenando em um vetor
medias = []
for aluno in notas:
    media = sum(aluno) / len(aluno)
    medias.append(media)

# Contando o número de alunos com média maior ou igual a 7
alunos_aprovados = sum(1 for media in medias if media >= 7)

# Imprimindo o número de alunos aprovados
print(f"\nNúmero de alunos com média maior ou igual a 7: {alunos_aprovados}")
