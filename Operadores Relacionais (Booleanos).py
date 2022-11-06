# Exercicio 1

funcionario = "Lucas Silva & Silva"
idade = 22
endereco = "Rua da Árvore Pau Brasil, nª 7 - São Paulo/SP"
profissao = "Estudante do ensino médio"
salario = 100.00

print("Nome: ", funcionario)
print("Idade: ", idade)
print("Endereço: ", endereco)
print("Profissão: ", profissao)
print("mesada: R$", salario, "\n") # "\n" = pula de linha; "\t" = tabulação, espaço

print("===================")

""" 
///////////////////////////////////////////////////////////////
"""

# Exercicio 2

print("Tipo de dado de funcionário ", type(funcionario))
print("Tipo de dado de idade ", type(idade))
print("Tipo de dado de endereço ", type(endereco))
print("Tipo de dado de profissão ", type(profissao))
print("Tipo de dado de salário ", type(salario), "\n")

print("===================")

""" 
///////////////////////////////////////////////////////////////
"""

#Manipulação de Strings

# dimensão de string - len ( )

a = "Mauricio"
print("dimensão da string a = ", len("a b"))
print("dimensão de string com espaço = ", len("a b"))
print("dimensão de string vazia = ", len(""))

# acesso de caracteres de strings

print("primeira letra de Mauricio = ", a[0])
c = "a b"
print("o valorentre a e b = ", c[1])
d = "abc"
print("valor entre a e c = ", d[1])

# strings concatenadas

e = " Conceição Mario"
print("nome do professor", a + e)
print("M"*5)
print("-*" * 10 + "-")

print("===================")

""" 
///////////////////////////////////////////////////////////////
"""

#Operadores Relacionais

"""
Dados do tipo lógico: 
    True -> verdadeiro
    False -> falso
"""

# operadores relacionais

a = 1
b = 2
c = 2
print("a igual b - ", a == b)
print("a diferente de b - ", a != b)
print("b maior que a - ", b > a)
print("a menor ou igual a b - ", a <= b)
print("c maior ou igual a b - ", c >= b)

print("===================")

# Exemplo (Menezes, 2019):

nota = 8
media = 7

aprovado = nota >= media
print("resultado da verificação da aprovação = ", aprovado)

print("===================")

""" 
///////////////////////////////////////////////////////////////
"""

# Operadores Lógicos

"""
not = não
and = e
or = ou
"""

# declaração de variáveis do tipo lógico

V = True
F = False

# Exemplo para operador "not" (Menezes, 2019)
print("complemento de True = ", not V)
print("complemento de False = ", not F)
# Exemplo para operador "e" (Menezes, 2019)
print("True and True = ", V and V)
print("True and False = ", V and F)
print("False and False = ", F and F)
# Exemplo para operador "or" (Menezes, 2019)
print("True or True = ", V or V)
print("True or False = ", V or F)
print("False or False = ", F or F)

print("===================")

""" 
///////////////////////////////////////////////////////////////
"""

# Exercicio 3 a)

print("resultado de 'not True = ", not True)
print("resultado de 'False and not True' = ", False and not True)
print("resultado final de 'True or False and not True' = ", True or False and not True, "\n")
# Exercicio 3 b)
salario = 1654.32
idade= 13
print("salário > 1000 e idade > 18 = ", salario > 1000 and idade > 18, "\n")
# Exercicio 3 c)
print("1 > 2 and True or False = ", 1 > 2 and True or False)
print("10 > 3 and False or False = ", 10 > 3 and False or False)
print("5 > 1 and True or True = ", 5 > 1 and True or True, "\n")

print("===================")

""" 
///////////////////////////////////////////////////////////////
"""

# entrada de dados pelo console
idade = int(input("idade = "))
print(idade)
nome = input("nome: ")
print(nome)
salario = float(input("digite salario: R$"))
print(salario)

print("verificando idade ", idade < 55)
print("verificando nome ", nome == "Mauricio")
print("verificando salário ", salario >= 1698.88)

print("===================")

""" 
///////////////////////////////////////////////////////////////
"""

# Exercicio 4 

""" tipo de dado booleano """
v = True
print("tipo de dado booleano = ", type(v))

# Exercicio 4 - esboço de um sistema especialista
temperatura = int(input("temperatura = "))
dor_cabeca  = input("tem dor de cabeça = ")
coriza = input("tem coriza = ")
print("\n temperatura = ", temperatura)
print("tem dor de cabeça = ", dor_cabeca)
print("tem coriza = ", coriza)
gripe = temperatura > 37 and dor_cabeca or coriza
print("o paciente tem gripe = ", gripe)

print("===================")

""" 
///////////////////////////////////////////////////////////////
"""

# Exercicio 5

temperatura = int(input("Temperatura = "))
dor_cabeca = input("tem dor de cabeça = ")
coriza = input("tem coriza = ")
print("\ntemperatura = ", temperatura)
print("tem dor de cabeça = ", coriza)
gripe = temperatura > 37 and dor_cabeca
print("\no paciente tem gripe = temperatura > 37 and dor_cabeca", gripe)
gripe = dor_cabeca or coriza
print("\no paciente tem gripe = dor_cabeca or coriza", gripe)
gripe = temperatura > 37 and dor_cabeca or coriza
print("\no paciente tem gripe = temperatura > 37 and dor_cabeca or coriza", gripe)