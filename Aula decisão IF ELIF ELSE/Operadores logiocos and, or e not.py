# Operador AND

idade_lucas= 21
idade_pedro= 19

if (idade_lucas >= 18) and (idade_pedro >= 18): # as duas tem que ser verdadeiras 
    print("As duas condições são verdadeiras")

# Operador  OR

idade_lucas= 21
idade_pedro= 19

if (idade_lucas >= 18) or (idade_pedro >= 18): # um ou outro
    print("Pelo menos uma das condições é verdadeira")

# Operador NOT

idade_lucas= 16
idade_pedro= 19

if not(idade_lucas >= 18): #not inverte o valor
    print("Pelo menos uma das condições é verdadeira")
