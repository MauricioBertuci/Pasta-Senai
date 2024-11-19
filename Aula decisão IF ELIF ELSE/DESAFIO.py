#Advinhe o valor entre 1 e 10

impar= input("Seu numero é impar? ")
if impar == "s":
   primo = input("Seu numero é primo? ")
   if primo == "n":
    print("Seu numero é 9 !!")
   elif primo == "s":
        num3 = input("menor que 3 ? ")
        if num3 == "s":
          print( "seu numero é 1 !!") #resposta
          print("EU SABIA :/")
        elif num3 == "n":
            num5 = input("Menor que 5 ? ")
            if  num5 == "s":
              print("seu numero é 3 !!") #resposta
              print("EU SABIA :/")
            elif num5 == "n":
              num7 = input("Menor que 7 ? ")
              num7 == "s"
              print("Seu numero é 5 !!") #resposta
              print("EU SABIA :/")
            if num7 == "n": 
                 print('Seu numero é 7 !!') #resposta
                 print("EU SABIA :/")
elif impar == "n":
   maior9 = input("Seu numero é maior que 9 ? ")
   if maior9 == "s":
    print("Seu numero é 10 !!")
   elif maior9 == "n":
        maior7 = input("maior que 7 ? ")
        if maior7 == "s":
          print( "seu numero é 8 !!") #resposta
          print("EU SABIA :/")
        elif maior7 == "n":
            maior5 = input("Maior que 5 ? ")
            if  maior5 == "s":
              print("seu numero é 6 !!") #resposta
              print("EU SABIA :/")
            elif maior5 == "n":
              maior3 = input("Maior que 3 ? ")
              maior3 == "s"
              print("Seu numero é 4 !!") #resposta
              print("EU SABIA :/")
              if maior3 == "n": 
                 print('Seu numero é 2 !!') #resposta 
                 print("EU SABIA :/")        
else:
   print("Seu numero não existe ou não se encaixa nos padrões")          

   




