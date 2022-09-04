# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 12:04:13 2022

@author: mathe
"""

arroz = 5
feijao = 3
acucar = 2
batata = 3
oleo = 5
bolacha_agua_sal = 1
bolacha_maizena = 1
banana = 18
couve_flor = 2
leite_po = 2


vl_arroz = float(input("Digite o valor do kg do arroz: "))
vl_feijao = float(input("Digite o valor do kg do feijão: "))
vl_acucar = float(input("Digite o valor do kg do açúcar: "))
vl_batata = float(input("Digite o valor do kg do batata: "))
vl_oleo = float(input("Digite o valor do litro de óleo: "))
vl_bolachaAS = float(input("Digite o valor do pacote de Bolacha de Água e Sal: "))
vl_bolachaM = float(input("Digite o valor do pacote de Maizena: "))
vl_couve = float(input("Digite o valor do maço de Couve-Flor: "))
vl_leitepo = float(input("Digite o valor da lata Leite em Pó: "))
print(" ")

print(" =======================================  ")

print(" ")

print("O valor dos produtos são")

print("O valor do KG de arroz é de: ", vl_arroz)
print(" ")
print("O valor do KG do Feijão é de: ", vl_feijao)
print(" ")
print("O valor do KG do Açúcar é de: ", vl_acucar)
print(" ")
print("O valor do KG da Batata é de: ", vl_batata)
print(" ")
print("O valor do Litro de Óleo é de: ", vl_oleo)
print(" ")
print("O valor do PACOTE de Bolacha de água e sal é de: ", vl_bolachaAS)
print(" ")
print("O valor do PACOTE de Bolacha de maizena é de: ", vl_bolachaM)
print(" ")
print("O valor do MAÇO de Couve-flor é de: ", vl_couve)
print(" ")
print("O valor da LATA de Leite em Pó é de: ", vl_leitepo)

print(" ")

print(" =======================================  ")

print(" ")

print("O preço dos produtos são")

print(" ")

pr_arroz = vl_arroz * arroz
pr_feijao = vl_feijao * feijao
pr_acucar = vl_acucar * acucar
pr_batata = vl_batata * batata
pr_oleo = vl_oleo * oleo
pr_bolachaAS = vl_bolachaAS * bolacha_agua_sal
pr_bolachaM = vl_bolachaM * bolacha_maizena
pr_couve = vl_couve * couve_flor
pr_leitepo = vl_leitepo * leite_po

print("O preço de 5KG de Arroz é de: ", pr_arroz)
print(" ")
print("O preço de 3KG de Feijão é de: ", pr_feijao)
print(" ")
print("O preço de 2KG de Açúcar é de: ", pr_acucar)
print(" ")
print("O preço de 3KG de Batata é de: ", pr_batata)
print(" ")
print("O preço de 5 Litros de Óleo é de: ", pr_oleo)
print(" ")
print("O preço de 1 PACOTE de Bolacha de água e sal é de: ", pr_bolachaAS)
print(" ")
print("O preço de 1 PACOTE de Bolacha de maizena é de: ", pr_bolachaM)
print(" ")
print("O preço de 2 MAÇOS de Couve-Flor é de: ", pr_couve)
print(" ")
print("O preço de 2 Latas de 1KG de Leite em Pó é de: ", pr_leitepo)
print(" ")

vl_total = pr_arroz + pr_feijao + pr_acucar + pr_batata + pr_oleo + pr_bolachaAS + pr_bolachaM + pr_couve + pr_leitepo

print(" ")

print("O valor total da compra foi de: R$ ", vl_total)

print(" ")

print(" =======================================  ")

print(" ")

print("Recomendado para gastar R$ 200.00")

print(" ")

if(vl_total < 200.00):
    print("Pagamento em Dinheiro")
else:
    print("Pagamento em parcelas com uso de cartão")    
