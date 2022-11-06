Lista = [8, 16, 20, -3]
for i in Lista:
    print(i)
    
print("===================")

""" 
///////////////////////////////////////////////////////////////
"""



#pesquisa a um elemento de lista com for

numero_lista = int(input("\ndigitar numero da lista que deseja pesquisar: "))
for i in Lista:
    if i == numero_lista:
        print("elemento pesquisando = ", i)
        break
    else:
        print("elemento não encontrado!")

print("===================")

""" 
///////////////////////////////////////////////////////////////
"""

# Exericico 2

print("\n\nexercício da lista com while")
j = 0
while j < len(Lista):
    i = Lista[j]
    print(i)
    j += 1
    
print("===================")

""" 
///////////////////////////////////////////////////////////////
"""

#pesquisa a um elemento de lista com while

numero_lista = int(input("\ndigitar numero da lista que deseja pesquisar: "))
numero_encontrado = False
k = 0
while k < len(Lista):
    if Lista[k] == numero_lista:
        numero_encontrado = True
        break
    k += 1
if numero_encontrado:
    print(f"{numero_lista} achado na posição {k}")
else:
    print("numero não encontrado!")
    
print("===================")

""" 
///////////////////////////////////////////////////////////////
"""

for i in range(10):
    print (i)
print ("\n")
for i in range(3, 8):
    print(i)

print("===================")

""" 
///////////////////////////////////////////////////////////////
"""

print("\n")
for i in range(0, 11, 2):
    print(i, end=" ")
    
print("===================")

""" 
///////////////////////////////////////////////////////////////
"""

print("\n")
lista_gerador = list(range(10, 101, 10))
print("lista_gerador = ", lista_gerador)

print("===================")

""" 
///////////////////////////////////////////////////////////////
"""

print("\n")
lista_gerador = list(range(10, 101, 10))
print("lista_gerador = ", lista_gerador)

soma = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print("\n")
lista_pares = list(range(0, 20, 2))
print("lista_pares = ", lista_pares)
lista_impares = list(range(1, 20 ,2))
print("lista_impares = ", lista_impares)
for i in range (10):
    soma[i] = lista_pares[i]+lista_impares[i]
print("lista com a soma dos impares e pares entre 0 e 20 = ", soma)