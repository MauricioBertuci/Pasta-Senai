#Criando uma lista de fruta
frutas = ["maçã", "banana","laranja", "manga" ]
print(f"Lista original: {frutas}")
print("."*30)


#Adicionando uma fruta no final lsita/vetor
frutas.append("uva") #.append Adiciona algo na lista
print(f"Após adicionar uva; {frutas}")
print("."*30)

#inserindo uma fruta em uma posição
frutas.insert(2,"morango")
print(f"Após inseriri o morango na posição 2: {frutas}")
print("."*30)

#Remover uma fruta pelo nome
frutas.remove("banana")
print("Apos remover banana: {frutas} ")
print("."*30)

#Ordenando as frutas em ordem alfabetica
frutas.sort()
print(f"Lista em ordem alfabetica:  {frutas}")
print("."*30)

#Ivertendo a ordem da Lista
frutas.reverse()
print(f"Lista em ordem inversa: {frutas}")
print("."*30)

#Contar quantas vezes aparece uma fruta 
qtd = frutas.count("maçã")
print(f"A fruta maçã aparece: {qtd} na lista ")
print("."*30)

#Removendo a ulima fruta e armazenado em uma varaiavel
ultima_fruta = frutas.pop()
print(f"Após usar o pop(): {frutas}")
print(f"Fruta removida: {ultima_fruta}")
print("."*30)

#Removendo frutas dentro de um intervalo de indices
del frutas[0:2]
print(f"Após remover frtuas do indice 0 ao 1 {frutas}")
print("."*30)

#limpado todos os itens da lista
frutas.clear()
print(f"lista após ser limpa")
print("."*30)

#Adicionar outros elementos de outra lista
frutas.extend(["abacaxi", "pera", "melão", "kiwi"])
print(f"lista com frutas novas {frutas}")
print("."*30)

#Encontrar a posição de um intem
posição = frutas.index("melão")
print(f"a fruta melão estã na posição: {posição}")
print("."*30)


