# Exercicio 1 
media = 0.0
portugues = 8.0
matematica = 6.0
historia = 7.5

print ("valor da média = \t\t\t\t", media)
media = (portugues + matematica + historia)/3
print("valor da media atualizada = \t", media)

print("===================")

""" 
///////////////////////////////////////////////////////////////
"""
# Exercicio 2
media = (portugues + matematica)/2
print("\n\nvalor da media atualizada = \t", media)

print("===================")

""" 
///////////////////////////////////////////////////////////////
"""

# Exercicio 3

nome = input("\n digitar o nome do aluno \t")
sobrenome = input("digitar o sobrenome do aluno \t")
portugues = float (input("digitar a nota de portuges"))
matematica = float(input("digitar a nota de matematica"))
historia = float(input("digitar a nota de história"))
geografia = float(input("digitar a nota de geografia"))
educacao_fisica = float(input("digitar a nota de educação fisica"))
media = (portugues + matematica + historia + geografia + educacao_fisica)/5
print("\nNome do aluno\t", nome + "\t" + sobrenome)
print("Nota de Portugues \t", portugues)
print("Nota de matematica \t", matematica)
print("Nota de História \t", historia)
print("Nota de Geografia \t", geografia)
print("Nota de Educação Fisica \t", educacao_fisica)
print("Valor da média atualizada = \t", media)

print("===================")

""" 
///////////////////////////////////////////////////////////////
"""

# Exercicio 4

if media >= 5.0:
    print("estado da condição >= 5.0 \t", media >= 5.0)
    print("aluno Aprovado")
if media < 5.0:
    print("estado da condição < 5.0 \t", media < 5.0)
    print("aluno Reprovado")

print("===================")

""" 
///////////////////////////////////////////////////////////////
"""

# Exercicio 5 -> if - else

if media >= 5.0:
    print("estado da condição >= 5.0 \t", media >= 5.0)
    print("aluno Aprovado")
else:
    print("estado da condição < 5.0 \t", media < 5.0)
    print("aluno Reprovado")
    
# Exercicio 6

identificacao = input("Identificação: ")
endereco = input("Endereço: ")
cpf = input("CPF: ")
renda_anual = float(input("Renda Anual = R$"))
imposto_pago = float(input("Imposto Pago = R$"))
print("identificação: ", identificacao)
print("Endereço: ", endereco)
print("CPF: ", cpf)
print("Renda Anual = R$", renda_anual)
print("Imposto Pago = R$ ", imposto_pago)
if renda_anual <= 44000.00:
    imposto = 0.0
else:
    imposto = renda_anual * 0.15 - imposto_pago
print("valor do imposto = R$ ", imposto)

