# Inicialização do contador:
x = 1
while x <= 5:
    print(x, "\n")
    x = x + 1

print("===================")

""" 
///////////////////////////////////////////////////////////////
"""

fim_contagem = int(input("Digitar valor do contador = "))
x = 1
while x <= fim_contagem:
    print(x, "\n")
    x = x + 1
    
print("===================")

""" 
///////////////////////////////////////////////////////////////
"""

limite = int(input("entrar com o valor limite da contagem dos numeros pares"))
contador = 0
while contador <= limite:
    if contador % 2 == 0: #resto de contador dividido por 2 == 0 ??
        print(contador, "\n")
    contador = contador + 1
    
print("===================")

""" 
///////////////////////////////////////////////////////////////
"""

limite = int(input("Entrar com o valor limite da contagem dos numeros impares"))
contador = 0
while contador <= limite:
    if contador % 2 == 1: #resto de contador dividido por 2 = 0 ??
        print(contador, "\n")
    contador = contador + 1
    
print("===================")

""" 
///////////////////////////////////////////////////////////////
"""

num = int(input("entrar com o numero para tabuada de multiplicação"))
n = 1
while n <= 10:
    print(num, "\tx", n, "\t=", num*n, "\n")
    n = n + 1    

print("===================")

""" 
///////////////////////////////////////////////////////////////
"""

comando = "continuar"
n = 0
while comando != "parar":
    comando = input("entrar com o comando de continuar ou parar: \t")
    n = n + 1
    print(n, "\t", comando)

print("===================")

""" 
///////////////////////////////////////////////////////////////
"""

# Exercicio 5

senha = "abc"
n = 1
while n <= 3:
    entrada_usuario = input("entrar com sua senha\t")
    if entrada_usuario == senha:
        print("senha correta")
        break # -> sai do laço
    else:
        n = n + 1
        print("senha errada")
        
print("===================")

""" 
///////////////////////////////////////////////////////////////
"""

# Exercicio 6

b = int(input("quantos numeros irá somar???"))
n = 1
soma = 0
while n <= b:
    a = int(input("entrar com valor do nº a somar: "))
    soma = soma + a 
    n = n + 1
print ("valor da soma = ", soma)

print("===================")

""" 
///////////////////////////////////////////////////////////////
"""

#Exercicio 7

a = int(input("entrar com a variável 'a': "))
b = int(input("entrar com a variável 'b': "))
n = 0
c = 0

while n < b:
    c = c + a
    n = n + 1
    print("c =", c)
    print("n =", n)
print("valor da multiplicação de a x b = ", c)

print("===================")

""" 
///////////////////////////////////////////////////////////////
"""

#Exercicio 9

b = int(input("quantos numeros irá somar???"))
n = 1
soma = 0

while n <= b:
    a = int(input("entrar com valor do nº a somar: "))
    if a == 0:
        break
    soma += a #soma += a #variável soma vai acumulando os valores de "a" a cada iteração
    n = n + 1
print("valor da soma = ", soma)

print("===================")

""" 
///////////////////////////////////////////////////////////////
"""

# Exericico 10

n = 1
a = "sim"
while a == "sim":
    b = int(input("tabuada de que número???"))
    while n <= 10:
        print(b, " x ", n, " = ", b*n)
        n += 1
    n = 1
    a = input("continuar com a tabuada - sim ou não ??? " )