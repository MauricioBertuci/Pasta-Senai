#Faça um origrama que solicite dois numeros ao users (com decimais) Em seguida solicite que o usuario informa a operação matematica 

num1= float(input('Digite um numero decimal: '))
num2= float(input('Digite um outro nuemro decuimal: '))

print('--'*30) #tabela
operação= print('Solicite a operação desejada')
div= print('/')
soma= print('+')
sub= print('-')
mult= print('*')
print('--'*30)

escolha= input('Qual a aperação escolhida: ')

if escolha == 'divisão' or escolha == '/':
    solução=(num1/num2)
    print(f'De acordo com a escolha {solução:.2f}')

elif escolha == 'soma' or escolha == '+':
    solução=(num1+num2)
    print(f'De acordo com a escolha {solução:.2f}')

elif escolha == 'subitração' or escolha == '-':
    solução=(num1-num2)
    print(f'De acordo com a escolha {solução:.2f}')

else:
    solução=(num1*num2)
    print(f'De acordo com a escolha {solução:.2f}')