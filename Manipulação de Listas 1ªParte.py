colecao = ["\n\nMaria", 22, "anos e salário de R$", 1287.98]
print(colecao[0])
print(colecao[1])
print(colecao[2])
print(colecao[3])

print("===================")

""" 
///////////////////////////////////////////////////////////////
"""

notas = [4.7, 5.6, 8.9, 3.5, 6.6, 7.4, 8.0, 9.5]
soma = 0.0
i = 0
while i < 8:
    soma += notas[i]
    i += 1
print(f"média: {soma/i: 5.2f}")

print("===================")

""" 
///////////////////////////////////////////////////////////////
"""

notas = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
soma = 0.0
i = 0
while i < 8:
    notas[i] = float(input(f"entrar com o valor da nota {i}:"))
    soma += notas[i]
    i += 1
    print("valor parcial da soma das notas = ", soma)
print(f"média: {soma/i: 5.2f}")

print("===================")

""" 
///////////////////////////////////////////////////////////////
"""

notas = [0.0, 0.0, 0.0, 0.0, 0.0]
nota_escolhida = 0
i = 0
while i < 5:
    notas[i] = float(input(f"entrar com o valor da nota {i + 1}: \t"))
    i += 1
nota_escolhida = int(input("Qual a nota que deseja ver? = "))
print(f"nota escolhida foi a: {nota_escolhida}ª")
print("nota = ", notas[nota_escolhida - 1])

print("===================")

""" 
///////////////////////////////////////////////////////////////
"""

lista_0 = [1,2,3]
lista_1 = lista_0
print("lista_0 = ", lista_0)
print("lista_1 = ", lista_1)
lista_1 [0] = 4
lista_1 [1] = 5
lista_1 [2] = 6

# a atualização de valores tem de ser feita para cada elemento individualmente
print("novos  valores de lista_1 = ", lista_1)
print("lista[0] tem a mesma referencia de lista[1]: lista_0", lista_0)

print("===================")

""" 
///////////////////////////////////////////////////////////////
"""

lista_0 = [1,2,3]
lista_1 = lista_0[:]
print("lista_0 = ", lista_0)
print("lista_1 = ", lista_1)
lista_1 [0] = 4
lista_1 [1] = 5
lista_1 [2] = 6

print("novos  valores de lista_1 = ", lista_1)
print("lista[0] tem a mesma referencia de lista[1]: lista_0", lista_0)

print("===================")

""" 
///////////////////////////////////////////////////////////////
"""

#segmentação 9fatiamento de listas
lista_2 = [1, 2, 3, 4, 5, 6]
#[a:b] à esquerda dois pontos: posição do inicio do segmento; à direita dos pontos = posição final (não incluído)
print("\n\nLista_2[0:6] = lista completa ", lista_2[0:6])
print("Lista_2[:6] = lista ", lista_2[:-6])
print("Lista_2[:-1] = menos um elemento a partir do fim da lista ", lista_2[:-1])
print("Lista_2[:-2] = menos dois elemento a partir do fim da lista ", lista_2[:-2])
print("Lista_2[:-3] = menos três elemento a partir do fim da lista ", lista_2[:-3])
print("Lista_2[:-5] = menos cinco elemento a partir do fim da lista ", lista_2[:-5])
print("Lista_2[0:1] = um elemento a partir do fim da lista ", lista_2[0:1])
print("Lista_2[0:2] = dois elemento a partir do fim da lista ", lista_2[0:2])
print("Lista_2[0:3] = três elemento a partir do fim da lista ", lista_2[0:3])
print("Lista_2[0:5] = cinco elemento a partir do fim da lista ", lista_2[0:5])
print("Lista_2[0:6] = todos elementos da lista ", lista_2[0:6])
print("Lista_2[1:3] = entre o segundo e quarto ( não incluído ) elementos da lista ", lista_2[1:3])
print("Lista_2[1:4] = entre o segundo e quinto ( não incluído ) elementos da lista ", lista_2[1:4])
print("Lista_2[2:5] = entre o terceiro e quarto ( não incluído ) elementos da lista ", lista_2[2:5])
print("Lista_2[3:5] = entre o quarto e quarto ( não incluído ) elementos da lista ", lista_2[3:5])
print("Lista_2[4:5] = quinto elemento da lista ", lista_2[4:5])
print("Lista_2[5:6] = sexto elemento da lista ", lista_2[5:6])
print("Lista_2[5:7] = sexto elemento da lista", lista_2[5:7])

print("===================")

""" 
///////////////////////////////////////////////////////////////
"""

frase = ["que optaram", "na estrada", "por viver", "filme", "NomadLand", "que conta", "de pessoas", "a historia", "é um"]
print("\n\n A frase ordenada é: ", frase[4:5], " ", frase[8:9], " ", frase[3:4], " ", frase[5:6], " ", frase[7:8], " ", frase[6:7], " ", 
      frase[0:1], " ", frase[2:3], " ", frase[1:2])
