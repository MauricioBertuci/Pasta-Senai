#Digite a senha e confirme ela
#As duas senhas digitadas são iguais ?
#A swenha tem pelo menos 8 caracteres
#Deve conter pelo menos uma letra maiuscula e um numero

"""
senha= input("Digite sua senha:  ")  
verificação= input("Digite sua senha novamente:  ")

#criterios de aprovação
tamanho_senha = len(senha)

if senha == verificação and tamanho_senha >= 8:
    pass
elif senha.isupper():
    pass 
elif senha.islower():
    pass
elif senha.isdigit() == True or senha.isalpha() == True:
    pass
else:
    print("Revise os parametros de analise !!")

print("Senha correta !!")
"""

senha= input("Digite sua nova senha:  ")  
verificação= input("Confirme sua nova senha:  ")


tamanho_senha = len(senha)


#Validando se é a msm senha
while True:
    if senha != verificação :
        senha= input("Digite novamente sua senha para verificar :  ")  
        verificação= input("Digite uma senha que condiz com a primeria:  ")

#Validar se é maior que 8 carcteres

 





# len() usado para contar o tamanho do texto 
# isupper() verifica se todos estão em maiuscula
# islower() verifica se toods estão em minusculo
# isdigit() usado para ver se todos os caracteres é digito
