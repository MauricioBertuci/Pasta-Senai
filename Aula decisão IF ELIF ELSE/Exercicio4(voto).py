#calcule a obritoriedade do voto para uma pessoa dependenod da idade

idade= int(input("DIGITE SUA IDADE: "))

if (idade >= 16) and (idade < 18) or (idade >= 70):
    print('Seu voto é facultativo !!')

elif idade < 16:
    print('Não vota!!')

else:
    print('Voto Obrigatorio !!')