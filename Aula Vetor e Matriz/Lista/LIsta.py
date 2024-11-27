"""#Criando lista 
bancos = ["Banco do Brasil", "Caixa", "Santander" ] #saida: ['Banco do Brasil', 'Caixa', 'Santander']
#Criando lista vazia 
meu_vetor = []

print(type(bancos))
print(bancos)

#Alterando um valor da lista
bancos[1] = "Inter"

#Alterando o ultimo item da lista
bancos[-1] = "C6"

print(bancos) #saida: ['Banco do Brasil', 'Inter', 'C6'] 

#Primeira forma de percorrrer
#Percorrer os valores do vetor
for banco in bancos:
    print(banco)
bancos = bancos + ["Bradesco", "Nubank"]
# ou bancos += ["Bradesco", "Nubank"] 
print(bancos)
"""

#Outra forma de percorrrer
#Percorrendo os valores com for
cores = ["vermelho","azul","verde" ]
for i in range(len(cores)):  #len()= tamanho
    cor = cores[i]
    print(f"Cor no índice {i} é: {cor}")

    