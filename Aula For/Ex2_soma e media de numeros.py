#Faça um programa q leia 5 numeros e informe a soma e a media dos numeros:

# Forma1
qtd_pessoas=5
soma = 0
for i in range(1,qtd_pessoas+1):
    valor= int(input(f"Digite o numero {i}: "))
    soma = soma + valor
    media= soma/qtd_pessoas
print(f"A soma de todos os numeros é {soma}")
print(f"A media de todos os numeros é {media}")
#-----------------------------------------------------------------------------------------------