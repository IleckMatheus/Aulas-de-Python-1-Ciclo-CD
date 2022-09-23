"""

Exercicio 1: Escrever código Python para testar os valores das variáveis A à F na tabela e
mostrar os resultados no console, para a expressão: Inserir os valores pelo console.
A >= B or not C or D > E and F

"""

A1 = 2.4
A2 = -3.6
A3 = 1.1
A4 = 7.8

B1 = 2.5
B2 = -3.59
B3 = 1.1
B4 = 6.4

C1 = True
C2 = False
C3 = True
C4 = False

D1 = 0.6
D2 = -0.08
D3 = 3.0
D4 = 5.0

E1 = 0.9
E2 = -0.09
E3 = 3.0
E4 = -5.0

F1 = True
F2 = True
F3 = False
F4 = True

print("\n==========================================================================\n")
print("A =",A1)
print("B =",B1)
print("C =",C1)
print("D =",D1)
print("E =",E1)
print("F =",F1, "\n")
respA1 = print("2.4 <= 2.5 True ou 0.6 > 0.9 True - ",A1 <= B1 or not C1 or D1 > E1 and F1, "\n")

print("\n==========================================================================\n")

print("A =",A2)
print("B =",B2)
print("C =",C2)
print("D =",D2)
print("E =",E2)
print("F =",F2, "\n")

respA2 = print("-3.6 <= -3.59 True ou -0.08 > -0.09 True - ",A2 <= B2 or not C2 or D2 > E2 and F2,"\n")

print("\n==========================================================================\n")

print("A =",A3)
print("B =",B3)
print("C =",C3)
print("D =",D3)
print("E =",E3)
print("F =",F3, "\n")

respA3 = print("1.1 <= 1.1 True ou 3.0 > 3.0 True - ", A3 <= B3 or not C3 or D3 > E3 and F3, "\n")

print("\n==========================================================================\n")

print("A =",A4)
print("B =",B4)
print("C =",C4)
print("D =",D4)
print("E =",E4)
print("F =",F4,"\n")

repsA4 = print("7.8 <= 6.4 True ou 5.0 > -5.0 True - ", A4 <= B4 or not C4 or D4 > E4 and F4, "\n")


print("\n==========================================================================\n")