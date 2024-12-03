    #Começa contar a partir do 0,1,2,3...
#Matriz é vetor dentro de vetor
"""
matriz= [
    [1,2,3], #linha 0
    [4,5,6], #linha 1
    [7,8,9] #linha 2
]
print(len(matriz))
print(matriz[0][1]) #Elemento da primeria linha, na segunda coluna: 2
print(matriz[1][2]) #Elemento da primeria linha, na segunda coluna: 6
"""

#Percorrendo uma matriz 3x3
"""
matriz= [
    [1,2,3] ,
    [4,5,6] ,
    [7,8,9] 
]
#i;cada linha
#j;cada coluna 

print(f"Tamanho da matriz: {len(matriz)}")
print("Elemtos da matriz: ")
for i in range(len(matriz)):
    print(f"linha: {i}")
    for j in range(len(matriz[i])):
        print(f"coluna: {j}")
        print(f"Posição: [{i}] [{j}] ")
"""
#Criar uma matriz 3x3 com valores forncidos pelo usuario

matriz= []
print("Preencha a matriz 3x3 \n ")
for i in range(3):
    linha= []
    for j in range(3):
        valor= int(input(f"Digite o valor para posição: [{i}][{j}]: ")) #coloca o valor em casa posição da linha, que tem 3 colunas
        linha.append(valor) 
    matriz.append(linha)    

print("Matriz")
for linha in matriz:
    print(linha)