# Imprimir gol da Alemanha 7 vezes 

"""
print("Gola da Alemanha !")
print("Gola da Alemanha !")
print("Gola da Alemanha !")
print("Gola da Alemanha !")
print("Gola da Alemanha !")
print("Gola da Alemanha !")
print("Gola da Alemanha !")
"""
#-------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------
# em vez disso, devemos usar While
"""
gols= 0

while gols < 7: #ler while como "enquanto tal coisa...
    gols = gols + 1
    print("Gol da Alemanha !")
print("Gol do Brasil !")
"""
#-------------------------------------------------------------------------------------------------------------------------------------------------------
'''
valor = 0

while valor < 10:
    print(valor)
    valor = valor + 1
'''
#-------------------------------------------------------------------------------------------------------------------------------------------------------
"""
contador = 1
soma = 0

while contador <=5:
    soma = soma + contador
    contador = contador + 1
    print(f"A soma é {soma}")
print(f"A soma final é {soma}")
"""
#-------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------
#usando Else no While 

"""
x = 0 
while x < 10:
    print(f"O valor de X nesta iteração é {x}")
    print("X ainda é menor que 10, somando 1 a X")
    print("-"*10)
    x = x + 1
else:
    print("Acabou o LOOP !!")
print(f"O ultimo valor é {x}")
"""
#-------------------------------------------------------------------------------------------------------------------------------------------------------
"""
valor = int(input("Quanto é 2 + 2 ? "))

while valor != 4:
    print("Errou, VAI ESTUDAR BURRO !!")
    valor = int(input("Quanto é 2 + 2 ? "))
else:
    print("Acertou irmão !!")
"""
#-------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------
#Pass, Break
"""
valor= 0

while valor < 10:
    if valor == 4:
        break #PARA PARAR O CODIGO !!
    else:
        #Nehuma ação especifica 
        pass #uma opção nula
    print(valor)
    valor = valor + 1
print(f"O valor {valor} foi achado !!")
"""

#-------------------------------------------------------------------------------------------------------------------------------------------------------
#Media da sala de aula usando While 
#Quando ultilizar O "While True" tem que usar "break"
"""
notas = 0
qtd_notas = 0

while True: #usado para forçar a tentradar do While
    nota = float(input("Informe a nota (-1 para finaliar): "))
    if nota == -1:
        break # quando colocar "-1" o programa irá parar
    notas += nota
    #notas = notas + notas
    qtd_notas += 1
 
    #qnt_notas = qnt_notas + 1
if qtd_notas > 0:
    media = notas/qtd_notas
    print(f"Quantidades de notas {qtd_notas}")
    print(f"A media das notas: {notas / qtd_notas:.2}")
else:
    print("Nenhuma nota informada !")
"""

"""
teste = input("Digite sim: ").upper() #le tudo minusculo
teste = input("Digite sim: ").lower
teste = input("Digite sim: ").capitalize() #Deixa a primeira letra maiusculo 

print("teste 1")
print("teste 2")
print("teste 3")
"""