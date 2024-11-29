#Digite a senha e confirme ela
#As duas senhas digitadas são iguais ?
#A swenha tem pelo menos 8 caracteres
#Deve conter pelo menos uma letra maiuscula e um numero

# len() usado para contar o tamanho do texto 
# isupper() verifica se todos estão em maiuscula
# islower() verifica se toods estão em minusculo
# isdigit() usado para ver se todos os caracteres é digito

def verificar_senha(senha, senha_confirmacao):
    # Verifica se as duas senhas são iguais
    if senha != senha_confirmacao:
        return "As senhas não são iguais."

    # Verifica se a senha tem pelo menos 8 caracteres
    if len(senha) < 8:
        return "A senha deve ter pelo menos 8 caracteres."

    # Verifica se a senha contém pelo menos uma letra maiúscula
    if not any(letra.isupper() for letra in senha):
        return "A senha deve conter pelo menos uma letra maiúscula."
    
    # Verifica se a senha contém pelo menos um número
    if not any(letra.isdigit() for letra in senha):
        return "A senha deve conter pelo menos um número."
    
    # Verifica se a senha não contém apenas letras minúsculas ou apenas números
    if senha.islower():
        return "A senha não pode conter apenas letras minúsculas."
    if senha.isdigit():
        return "A senha não pode conter apenas números."

    return "Senha válida!"

senha = input("Digite a senha: ")
senha_confirmacao = input("Confirme a senha: ")

resultado = verificar_senha(senha, senha_confirmacao)
print(resultado)
