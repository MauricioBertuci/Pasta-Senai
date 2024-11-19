#tabuada
while True: 
    nmr= int(input("Escolha um numero para treinar a tabuada: "))
    contador= 1
    erros= 0
    acertos= 0

    while contador <=10:
        pergunta= int(input(f"Digite o resultado de {nmr}X{contador} "))
        calculo= nmr*contador
        contador +=1
        if pergunta == calculo:
            print("Acertou! ")
        else:
            print(f"Resposta errado, a resposta correta é {calculo}")
        if pergunta == calculo:
            acertos += 1
        else:
            erros += 1
    print(f"Sua quantidade de erros é de {erros} e a quantidade de acerto é de {acertos}")
    pergunta2=input("Deseja jogar denovo [S/N]").upper()

    if pergunta2 == "N":
        print("Obrigado e até a proxima :)")
    else:
        print("Vamos para mais uma :)")
    contador=1
    erros=0
    acertos=0
















