'''for i in range(5,7,1): #range(inicio"5",fim "7",salto"1")
    print("GOL da Alemanha")
'''
'''
#usando range
for i in range(3):
    print(i) #cmc do 0 ent vai ir até "2"

#imprimir de 0 a 11
#range(inicio,fim,salto)
for contador in range(0,11,2):
    print(contador)
'''
'''
nome= "Mauricio"
for i in nome:
    print(i) #printa na vertical
'''
'''
notas_alunos= [10,9,8,7,3]
#for(para cada) i(item) in(dentro) lista-
for i in notas_alunos:
    print(i)
'''
'''
#usando Break 
for gol in range(1000):
    print("Dol da Alemanha")
    if gol == 6:
        break
print("Chegaaa")
print("Gol do Brasil")
'''
'''
#usando comando continue e else
for i in [1,10,20,30,40,50]:
    if i == 30:
        continue
else:
    print("acabou")
'''
#-----------------------------------------------------------------------------------------
#somando os valores limitado a 50.
inicio=int(input("Digite o primeiro numero: "))
fim=int(input("Digite o lutimo numero:"))
salto=int(input("Digite o salto:"))
total=0
texto= 'calculo'

for numero in range(inicio,fim,salto):
    total = total + numero #ou total +=numero
    texto = texto + str(numero )
    if numero >=50:
        break
    if numero != fim-1:
        texto = texto + " + "
print(texto)
print(total)

#---------------------------------------------------------------------------------------------
#media da sala

qtd_alunos= int(input("Digite quantos alnunos tem na sala: "))
total=0
for aluno in range(qtd_alunos):
    nota= float(input(f"Digite a nota do {aluno+1}° aluno: "))
    total += nota
print(f"A media da turma é: {total/qtd_alunos}")