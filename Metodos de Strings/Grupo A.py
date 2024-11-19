#in procura algo dentro da lista

lista=[1,2,3,4,5]
num= int(input("Digite um valor: "))
if num in lista:
    print("Temos esse valor !!")
else:
    print("Não temos esse valor !!")

#lower() deixa tudo minusculo

lower= input("Digite uma palavra: ").lower()
print(lower)

#isalnum() verifica se tem caracteres especiais

entrada= input("Digite numeros ou letras: ")
if entrada.isalnum():
    print("Bouaaaa")
else:
    print("Erroo !!!")

#title() deixa todas a primeiras letras Maisculas 

texto= input("Digite uma frase: ")
novo_texto = texto.title()
print(novo_texto)

#find() entra a primeria vez que aparece a string

texto= input("Digite um frase: ")
procurar= input("qual palavra quer procurar: ")
ache_string = texto.find(procurar)
print(ache_string)

#rfind() entra a ultima vez que aparece a string

texto= input("Digite um frase: ")
procurar= input("qual palavra quer procurar: ")
ache_string = texto.rfind(procurar)
print(ache_string)






#in {analisa se tem algum dentro de uma lista}
print("procura dentro de uma lista !!" )
lista= [1,2,3,4]
num=1
print(num in lista)
print("."*30)

#lower {Deixa tudo minusculo}
print("Deixa tudo minusculo !!" )
frase= "HOLLA MUNDO !!"
print(frase.lower())
print("."*30)


#isalnum() {verifica se tem caracteres especiais}
print("verifica se tem caracteres especial !!" )
frase= "HOLLA MUNDO !!"
print(frase.isalnum())
print("."*30)


#title() {deixa todas a primeiras letras Maisculas }
print("Deixa todas as primeira letras maiuscula !!" )
frase= "HOLLA MUNDO !!"
print(frase.title())
print("."*30)


#find() {Ache a primeira vez usada}
print("Acha a premeira vez que usou !!" )
frase= "eu sou feliz e eu sou legal "
procurar= "eu"
ache_primeira_string = frase.find(procurar)
print(ache_primeira_string)
print("."*30)


#rfind() {Acha a ultima vez usada}
print("Acha a ultima vez que usou !!" )
frase= "eu sou feliz e eu sou legal "
procurar= "eu"
ache_ultima_string = frase.find(procurar)
print(ache_ultima_string)
print("."*30)
