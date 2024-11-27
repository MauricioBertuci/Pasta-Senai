"""# Verifica se as senhas são iguais
if senha != confirmar_senha:
    print("As senhas não coincidem. Tente novamente.")
    return

    # Verifica se a senha tem pelo menos 8 caracteres
if len(senha) < 8:
    print("A senha deve ter pelo menos 8 caracteres.")
    return

    # Verifica se a senha contém pelo menos uma letra maiúscula
if not any(char.isupper() for char in senha):
    print("A senha deve conter pelo menos uma letra maiúscula.")
    return

    # Verifica se a senha contém pelo menos um número
if not any(char.isdigit() for char in senha):
    print("A senha deve conter pelo menos um número.")
    return
print("Senha válida!")

# Chama a função para validar a senha
validar_senha()
"""