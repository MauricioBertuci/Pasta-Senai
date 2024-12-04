#def é um bloco de nota reultilizavel
#como funciona:

#def nome_da_função
    #instrução 1
    #instrução 2
    #instrução ...
    #instrução ...
    #retourn valor (opcional)

#Exemplo comprimento
"""
def great():
    print("Hi my friend !!")

great()
"""
#Exemplo soma
"""
def soma(a,b):
    return a + b

resulado = soma(2,3)
print(resulado)
"""
#Exemplo 

def saudação(nome= "Visitante"):
    return f"Olá {nome}"

print(saudação("Maria")) #saida: Olá maria 
print(saudação()) #saida: Ola Visitante


#Exemplo Imposto
"""
def calcula_imposto(valor):
    if valor < 1000:
        imposto = valor * 0.1
    elif valor < 2000:
        imposto = valor * 0.13
    else:
        imposto = valor * 0.2
    return imposto

preço_produto1 = 2000
preço_produto2 = 1000
imposto_produto1 = calcula_imposto(preço_produto1)
imposto_produto2 = calcula_imposto(preço_produto2)

print(preço_produto1)
print(preço_produto2)
"""
