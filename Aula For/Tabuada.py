#Escreva um algoritimo que solicite ao usuario um nuemro e calculae mostra a tabuada dessse numero 

# Forma 1
print("Vamos fazer a tabuada!! ")
valor= int(input("Digite um valor: "))
tabuada=0

print("\n")
print(f'Tabuado do numero {valor}')
print("--"*30)

for tabuada in range(1,11,1):
    resultado= tabuada * valor 
    tabuada += 1
    print(f"{valor}x{tabuada}= {resultado}")
print("--"*30)
#-----------------------------------------------------------------------------------------------------
# Forma 2
numero= int(input("Digite um valor para tabuada: "))
tabuada_forma2=0

for tabuada in range(1,11):
    resultado = tabuada_forma2 * numero 
    tabuada_forma2 += 1 
    print(f"{numero}X{tabuada_forma2}= {resultado}")
#------------------------------------------------------------------------------------------------
#Forma 3

num= int(input("Digite um valor para tabuada: "))
for i in range(1,11):
    print(f"{num}X{i} = {num*i}")
#------------------------------------------------------------------------------------------------

#Vai dizer se esta certo ou errado

vm =int(input("Digite um numero para treinar a tabuada: "))
tabuada_forma3=0