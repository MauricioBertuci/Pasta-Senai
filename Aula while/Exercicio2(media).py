#Faça um progrmaa que calcule e mostre a media aritimetica de N notas 

soma=0
q_notas=0
while True: 
    nota = float(input("Informe a nota (-1 para finaliar): "))
    if nota == -1:
        print("Todas as notas foram colocadas !")
        break
    soma += nota
    q_notas += 1
    #print(soma)
    #print(q_notas)
    media= soma/q_notas
    print(f"A Media esté em {media:.2} do aluno.") 
print("--"*20)
print(f"A Media final do aluno é de {media:.2}.") 
print("--"*20)

