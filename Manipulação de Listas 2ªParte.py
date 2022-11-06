frase = ["que optaram", "na estrada", "por viver", "filme", "NomadLand", "que conta", "de pessoas", "a historia", "é um"]

#função len(lista) retorna o tamanho (dimensão) da lista
print(f"\n\na lista com a frase \n 'NomadLand é um filme que conta a história de pessoas que \noptaram por viver na estrada' tem {len(frase)}")

print("===================")

""" 
///////////////////////////////////////////////////////////////
"""

comentario = ["As formigas", "trabalham", "durante", "o ano inteiro.", "As cigarras", "aparecem", "no verão."]
dimensao_comentario = len(comentario)
i = 0
while i < dimensao_comentario:
    print(comentario[i])
    i += 1
print('\nsó as formigas!')
comentario_formigas = comentario[0:4]
dimensao_comentario_formigas = len(comentario_formigas)
j = 0
while j < dimensao_comentario_formigas:
    print(comentario_formigas[j])
    j += 1
print('\nsó as cigarras!')
comentario_cigarras = comentario[4:7]
dimensao_comentario_cigarras = len(comentario_cigarras)
k = 0
while k < dimensao_comentario_cigarras:
    print(comentario_cigarras[k])
    k += 1

print("===================")

""" 
///////////////////////////////////////////////////////////////
"""

print("\n\nO tamanho atual da lista 'comentário é: ", len(comentario))
comentario.append("As Joaninhas não tem nada a ver com isso.")
print ("'comentario' aumentou para ", len(comentario), "elementos")
print(comentario)

print("===================")

""" 
///////////////////////////////////////////////////////////////
"""

salarios = []
while True:
    valores = float(input("entrar com valor de salário - se valor negativo - encerrar: "))
    if valores < 0:
        break
    salarios.append(valores)
print("a lista 'salários' tem ", len(salarios), 'salários')
i = 0
while i < len(salarios):
    print(f"R$ {salarios[i]:5.2f}")
    i += 1
    
print("===================")

""" 
///////////////////////////////////////////////////////////////
"""

numeros = []
print("a lista 'numeros' tem ", len(numeros), numeros)
numeros = numeros + [1]
print("a lista 'numeros' tem ", len(numeros), numeros)
numeros = numeros + [3]
print("a lista 'numeros' tem ", len(numeros), numeros)
numeros = numeros + [-5]
print("a lista 'numeros' tem ", len(numeros), numeros)

print("===================")

""" 
///////////////////////////////////////////////////////////////
"""

numeros = []
print("a lista 'numeros' tem ", len(numeros), numeros)
numeros = numeros + [1]
print("a lista 'numeros' tem ", len(numeros), numeros)
numeros = numeros + [3]
print("a lista 'numeros' tem ", len(numeros), numeros)
numeros = numeros + [-5]
print("a lista 'numeros' tem ", len(numeros), numeros)
del numeros[1]
print("a lista 'numeros' tem ", len(numeros), numeros)
print(numeros[0])
print(numeros[1])