#Faça um programa criando um loop infinito onde o user terá que reponder se gosta de Python 
#caso responder qq coisa diferente de "sim" colocar "esta não é a resposta correta"
#caso reponder que "gosto" colocar "esta é a resposta correta"

resposta= input("Você gosta de Python, se gosta digite sim: ").upper()

while resposta != "SIM":
    print("Está resposta está errada !!")
    resposta= input("Você gosta de Python, se gosta digite sim: ").upper()
else:
     print("Sua resposta esta correta !")  
    
#pode usar tambem o While true

while True:
     resposta= input("Voce gosta de Python: ").upper()

     if resposta == "SIM":
          print('resposta certa !!')
          break
     else:
        print("Podii não homi !!")

    


