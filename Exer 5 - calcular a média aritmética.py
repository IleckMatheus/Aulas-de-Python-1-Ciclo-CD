"""
Exercício 5: Construir código em Python que possa calcular a média aritmética 
do aluno selecionado e retornar no console se 
o mesmo está aprovado (média >= 5.0) ou reprovado. 
Mostrar no console todas as notas do aluno selecionado 
→ utilizar elif para selecionar o aluno.
Historia    Geografia   Portugues   Matematica  Ciencias    Literatura  Aluno
 5.6           6.7         7.0         10.0       4.0          8.0      Maria   
 2.3           6.6         8.0         5.5       10.0          5.0      Tânia
 7.7           4.0         7.0         7.9        2.2          6.5      José
 9.0          10.0         3.3         8.0        6.0          4.6      Daniel
"""

alunos = input("Digite o nome do aluno: ")

maria = "Maria"
tania = "Tânia"
jose = "José"
daniel = "Daniel"


if alunos == maria:
    
    Maria = (5.6 + 6.7 + 7.0 + 10.0 + 4.0 + 8.0) / 6
    mediaM = Maria
    
    print("\nA Maria tirou: ")
    print("5.6 em História")
    print("6.7 em Geografia")
    print("7.0 em Português")
    print("10.0 em Matemática")
    print("4.0 em Ciências")
    print("8.0 em Literatura")
    print("\nSua média foi de: ", mediaM)
    
    
    if mediaM >= 5.0:
        print("\nAprovada")
    else:
        print("\nReprovado")
        
elif alunos == tania:
    
    Tania = (2.3 + 6.6 + 8.0 + 5.5 + 10.0 + 5.0) / 6
    mediaT = Tania
    
    print("\nA Tânia tirou: ")
    print("2.3 em História")
    print("6.6 em Geografia")
    print("8.0 em Português")
    print("5.5 em Matemática")
    print("10.0 em Ciências")
    print("5.0 em Literatura")
    print("\nSua média foi de: ", mediaT)
    
    if mediaT >= 5.0:
        print("\n Aprovada")
    else:
        print("\n Reprovado \n")

elif alunos == jose:
    
    Jose = (7.7 + 4.0 + 7.0 + 7.9 + 2.2 + 6.5) / 6
    mediaJ = Jose
    
    print("\nA José tirou: ")
    print("7.7 em História")
    print("4.0 em Geografia")
    print("7.0 em Português")
    print("7.9 em Matemática")
    print("2.2 em Ciências")
    print("6.5 em Literatura")
    print("\nSua média foi de: ", mediaJ)
    
    if mediaJ >= 5.0:
        print("\nAprovada")
    else:
        print("\nReprovado \n")
        
elif alunos == daniel:
    
    Daniel = (9.0 + 10.0 + 3.3 + 8.0 + 6.0 + 4.6) / 6
    mediaD = Daniel
    
    print("\nA Daniel tirou: ")
    print("9.0 em História")
    print("10.0 em Geografia")
    print("3.3 em Português")
    print("8.0 em Matemática")
    print("6.0 em Ciências")
    print("4.6 em Literatura")
    print("\nSua média foi de: ", mediaD)
    
    if mediaD >= 5.0:
        print("\n Aprovada")
    else:
        print("\n Reprovado \n")
