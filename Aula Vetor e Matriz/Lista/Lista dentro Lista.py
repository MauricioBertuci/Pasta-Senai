"""compras = [10.5, 3.50, 28.5, ["tomate", "sabonete", "arroz"]]
print(compras)
produtos = compras[3]
print(produtos)

#somando os valores
total = compras[0] + compras[1] +compras[2]
print(total)

#Para verificar veriificar a existencia de um item na lista 
letras = ["a", "b", "c", "d", "e"]
var = input("informe uma letra: ").lower()
if var in letras:
    print(f"A letra {var} está na lista ")
else:
    print(f"A letra {var} não está na lista")

#Adicionar elementos na lista fornecido pelo usuario 
tarefas = [] 

tarefa = input("Digite uma tarefa: ")
tarefas.append(tarefa)
print(tarefas)

while tarefa != "":
    tarefa =input("Digite uma tarefa: ")
    tarefas.append(tarefa)
print(tarefas)

#--------------------------------------------------------

nova = []
while True:
    num = int(input("Digite um numero interio (o para sair)")) 
    if num == 0:
        break
    nova.append(num)

print(nova)
#Soma itens da lsita
print(sum(nova))
#Maior da valor da lista max()
print(max(nova))
#Menor valor da lista min()
print(min(nova))
"""
#----------------------------------------------------------------

produtos = [" apple tv ", " air pods ", " mac ", " iphone 15 ", " ipad "]

novo_produto = produtos.append(input("Digite o produto: "))

#removendo um item
item_removido = input("DIgite o produto que deseja remover: ").lower()

if item_removido in produtos:
    produtos.remove(item_removido)
    print("Produto removido! ")
else:
    print(f"O item {item_removido} não existe na lista !")

for i in produtos:
    print(i, end= "-")    