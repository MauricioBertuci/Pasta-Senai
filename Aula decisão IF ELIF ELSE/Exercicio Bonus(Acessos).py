#Escreva um programa que verifica o acesso de um usuário a um sistema com base em três critérios: 
# O usuário deve ter pelo menos 18 anos. Pode ser "admin", "usuario" ou "visitante". 
# Deve ser verificada para acesso de "admin" e "usuario".

idade=int((input('Digite sua idade: ')))
print('\n')

print('--'*30)
print('Escolha entre:')
print('admin')
print('usuario')
print('visitante')
user=input('Digite sua area de trabalho: ')
print('--'*30)
print('\n')

if (idade >= 18) and (user == "usuario"):
    senha_usuario=input('Digite a senha: ')
    if senha_usuario == "1234":
        print("Acesso concedido como usuário.")
    else:
        print('Senha incorreta para usuário.')

elif (idade >= 18) and (user == 'visitante'):
    print("Acesso concedido como visitante. ")

elif (idade >= 18) and (user == 'admin'):
     senha_admin=input('Digite a senha: ')
     if senha_admin == "admin1234":
        print("Acesso concedido como administrador.")
     else: 
        print('Senha incorreta para administrador')
else:
    print('Acesso negado. Você precisa ter 18 anos ou mais.')
