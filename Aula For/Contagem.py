#Entrar com sexo de varias pessoas e imprimir quantas pessaos vão do sexo masculino (m ou M)

qtd_pessoas= int(input("Digite a quantidade de pessoas: "))
contagem_masc= 0 
contagem_outro= 0

for i in range(1,qtd_pessoas+1):
    sexo= input(f"Digite da pessoas {i}(usando a primeira letra):  ") 
    if sexo == "m" or sexo == "M":
        contagem_masc += 1
    else: 
        contagem_outro
print(f"Ao todo tem {contagem_masc} pessoas do sexo masculino")

#Pedido nome e sexo
"""
qtd_pessoas= int(input("Digite a quantidade de pessoas: "))
contagem=0
pessoas=1
for pessoas in range(1,qtd_pessoas+1):
    pessoas=+ input(f"Digite seu nome {pessoas}: ")
    sexo= """