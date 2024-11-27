#Digite a senha e confirme ela
#As duas senhas digitadas são iguais ?
#A swenha tem pelo menos 8 caracteres
#Deve conter pelo menos uma letra maiuscula e um numero


senha= input("Digite sua senha:  ")  
verificação= input("Digite sua senha novamente:  ")

#criterios de aprovação
tamanho_senha = len(senha)

if senha == verificação and tamanho_senha >= 8 and senha.upper():
            print("Senha correta !!")
else:
    print("Revise os parametros de analise !!")
        
    

# len() usado para contar o tamanho do texto 
# isupper() verifica se todos estão em maiuscula
# islower() verifica se toods estão em minusculo
# isdigit() usado para ver se todos os caracteres é digito
