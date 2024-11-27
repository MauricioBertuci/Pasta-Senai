#Faça um programa que leie 4 notas, mostre as notas e a media 
notas = []
num = 0

while num < 4:
    notas.append(float(input(f"Digite a nota {num+1}: ")))
    num +=1
    
print(notas)
media= sum(notas)/4
print(f"A media do aluno é; {media} ")

