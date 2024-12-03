#Criando um estoque para 3 produtos com quantidade de cada e saida de cada
Estoque = []

#cada produto
for nome_produto in range(2): 
    linha = []

#quanidade de cada coisa pedida
    for quantidade in range(1):
        produto= input("Digite o nome do produto: ")
        entrada= int(input(f"Quantas unidade entraram do {produto}:"))
        saida= int(input(f"Quantas unidade sairam do {produto}:"))
        linha.append(produto)
        linha.append(entrada)
        linha.append(saida)
    Estoque.append(linha)

#Mostrando o matriz
print("[Produto-Entrada-Saida]")
for linha in Estoque:
    print(linha)