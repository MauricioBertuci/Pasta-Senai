#Faça um programa que verifique estado civil de uma pessoa. se a letra digitada é C (casada), S (solteira), D (divoricada), V (viuva)
# ou O (outros). confroam a letra escrita pelo usuario seu programa deve escreve o estado civil

print("--"*30)
print("TABELA PARA ESTADO CIVIL")
print('\n')
print('Digite "C" para casado')
print('Digite "S" para solteiro')
print('Digite "D" para divorsiado')
print('Digite "V" para viuvo')
print('Digite "O" para outros')
print("--"*30)

estado= input('De acordo com a tabela acima diga qual seu estado civil: ')
print("--"*30)
print('\n')

if estado == "C" or estado == "c":
    status= input('Voce é casado, correto ?')
    if status == "sim":
        print("BEM VINDO CASADO")
    else:
        print('VOLTE ANO INICIO')  


elif estado == "S" or estado =="s":
    status= input('Você é solteiro, correto ?')
    if status == "sim":
        print("BEM VINDO SOLTEIRO")
    else:
        print('VOLTE ANO INICIO')  


elif estado == "D" or "d":
    status= input('Você é divorciado, correto ?')
    if status == "sim":
        print("BEM VINDO DIVOCIADO")
    else:
        print('VOLTE ANO INICIO')  

   
elif estado == "V" or "v":
    status= input('Você é viuvo, correto ?')
    if status == "sim":
        print("BEM VINDO VIUVO")
    else:
        print('VOLTE ANO INICIO')  


else:
    status= input('Você não se encaixa em nenhum, correto ?')
    if status == "sim":
        print("BEM VINDO")
    else:
        print(
            'VOLTE ANO INICIO')  

    