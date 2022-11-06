qtd = int(input("Qual a quantidade de peças de roupa irá comprar? \t"))
if qtd <= 30 and qtd >= 20:
    prc_unidade = 28.00
if qtd < 20:
    prc_unidade = 35.00
if qtd > 30:
    prc_unidade = 20.00

print("\nquantidade de peças de roupa =\t", qtd)
print("\npreço por unidade de acordo com a quantidade = R$ ",prc_unidade)
print(f"\npreço da compra =: R$ {prc_unidade * qtd:8.2f}")
print("quantidade <= 30 and quantidade >= 20: ", qtd <= 30 and qtd >= 20)
print("quantidade < 20: ", qtd < 20)
print("quantidade > 30: ", qtd > 30)

#COMPOSIÇÃO DE STRINGS
#Formatação com f-string -> f"{variável e :nº caracteres}"
#:x.yf: x = nº de caracteres; y = nº decimal (usado para dinheiro)

print("===================")

""" 
///////////////////////////////////////////////////////////////
"""

#TABELA - CODIGO   PREÇO
#           1      13.30
#           2       1.40
#           3      19.00
#           4     123.79 
#           5      44.33

cd = int(input("digitar o código do produto\t"))
if cd == 1:
    prc_produto = 13.30
else:
    if cd == 2:
        prc_produto = 1.40
    else:
        if cd == 3:
           prc_produto = 19.00
        else:
            if cd == 4:
                prc_produto = 123.79
            else:
                if cd == 5:
                    prc_produto = 44.33
                else:
                    print("\ndigitar código do produto entre 1 e 5: código -> ", cd, "não válido!")
                    prc_produto = 0.00
print("\ncódigo do produto =\t\t\t\t\t\t\t\t\t", cd)
print(f"\npreço do produto de acordo com o código = R$ {prc_produto: 4.2f}")

print("===================")

""" 
///////////////////////////////////////////////////////////////
"""

# Exercicio 4

temperatura = float(input("Qual a temperatura ambiente em ºC?\t"))
clima =""
if temperatura > 30:
    clima = "Quente"
else:
    if temperatura > 16:
        clima = "Agradável"
    else:
        clima = "Frio"
print("\nTemperatura = \t", temperatura, " ºC")
print("\nEntão o clima está\t", clima)        

print("===================")

""" 
///////////////////////////////////////////////////////////////
"""

# Exercicio 5

estacao = input("Qual a estação do ano?\t")
meses = ""
if estacao == "Primavera":
    meses = "Setembro - Outubro - Novembro - Dezembro"
else:
    if estacao == "Verão":
        meses = "Dezembro - Janeiro - Fevereiro - Março"
    else:
        if estacao == "Outono":
            meses = "Março - Abril - Maio - Junho"
        else:
            if estacao == "Inverno":
                meses = "Junho - Julho - Agosto = Setembro"
print("\nEstação do Ano:\t", estacao)
print("\nCompreende os meses:\t", meses)

print("===================")

""" 
///////////////////////////////////////////////////////////////
"""

#TABELA - CODIGO   PREÇO
#           1      13.30
#           2       1.40
#           3      19.00
#           4     123.79 
#           5      44.33

cd = int(input("digitar o código do produto\t"))
if cd == 1:
    prc_produto = 13.30
elif cd == 2:
    prc_produto = 1.40
elif cd == 3:
    prc_produto = 19.00
elif cd == 4:
    prc_produto = 123.79
elif cd == 5:
    prc_produto = 44.33
else:
    print("\ndigitar código do produto entre 1 e 5: código -> ", cd, "não válido!")
    prc_produto = 0.00
print("\ncódigo do produto =\t\t\t\t\t\t\t\t\t", cd)
print(f"\npreço do produto de acordo com o código = R$ {prc_produto: 4.2f}")