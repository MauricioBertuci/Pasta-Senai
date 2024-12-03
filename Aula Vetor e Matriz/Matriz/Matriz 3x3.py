#Crie uma matriz 3x3 preeenchida com nuemros inteiros fornecidos pelo user
#some os elementos ds linhas 

matriz = []

print("Preenchendo matriz !!")

#pedindo valores da linha
for coluna in range(2):
    linha = []
    
#pedindo valores das colunas
    for posição in range(2):
        valor= int(input(f"Digite um numero da linha {coluna} na coluna {posição}: "))
        linha.append(valor)
    matriz.append(linha)

#mostrando a matriz completa
print("matriz")
for linha in matriz:
    print(linha)

#Soma linha
for linha in matriz:
    print(f"Soma da linha {linha} é {sum(linha)}")






