#Contrua um programa em ultilizando os comandos aprendidos até agora para encontrar todos os pares de 0 a 100

# Forma1
contador= 0 
for i in range(1,101):
    if i%2 == 0:
        contador+= 1
    print(f"O total de numero pares de 0 a 100 é de {contador}")
#--------------------------------------------------------------------------------------------------------    
# Forma2
contador= 0 

for pares in range(2,101,2):
    contador += 1
print(f"O total de pares é de {contador}")