# Aula 1 - Tipos de dados int e String

# Atribuições de valores a variáveis do tipo inteiro - int
a = 12
b = -8

""" 
///////////////////////////////////////////////////////////////
"""

# Atribuições de valores a variáveis do tipo string - str
c = "Ciência de Dados"
d = '@*$?'
e = ""
f = "88"

print("===================")

""" 
///////////////////////////////////////////////////////////////
"""

# comando de impressão no console: print

print("a = ",a)
print("b = ",b)
print("c = ",c)
print("d = ",d)
print("e = ",e)
print("f = ",f)

print("===================")

""" 
///////////////////////////////////////////////////////////////
"""

# Conversão de string para inteiro

h = int(f)
g = b + h

print("g = (-8) + 88 = ",g)

print("===================")

""" 
///////////////////////////////////////////////////////////////
"""

# conversão de inteiro para string

str(a)
a = c
print ("a: string = ", a)

print("===================")

""" 
///////////////////////////////////////////////////////////////
"""

# Referência de objeto: tipagem dinâmica

# Uma referência de objeto (=variável) assume o valor de um tipo de dado através do operador " = "
cor = "azul" #cor <- string azul
numero = 6 #numero <- número 6
print("a cor é: ", cor)
print("o numero é: ", numero)

# o valor do objeto (=variável) pode ser mutável, independente do tipo
#Python utiliza tipagem dinâmica

cor = numero
print("o número é: ", cor)

#redefinição dos valores
cor = "laranja"
numero = 19

#imprimindo os tipos de dados das variáveis - "\n" -> muda de linha
print("a cor é: ", cor, "\n tipo de dado: ", type(cor))
print("o número é: ", numero, "\n tipo de dado: ", type(numero))

""" 
///////////////////////////////////////////////////////////////
"""
