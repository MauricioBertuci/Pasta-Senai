#Faça um programa que calcule o numero medio de alunos por turma. para isto, peça a quantidade de turma e a quantidade de alunos por turma
# a turma nn pode passar de 40 pessoas

turmas= int(input("Digite a Quantidade de turmas: "))
contador= 0
soma= 0

while contador < turmas:
    alunos= int(input(f"Digite a quantidade de alunos da turma {contador +1}: "))
    if alunos <= 40:
        contador +=1
        soma += alunos  
    else: 
        print("O numero de alunos não pode assar de 40 !!")
print(f"A media das turmas é {soma/turmas:.0f}")



    
    
   




