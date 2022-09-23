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

respA1 = print("2.4 é menor igual que 2.5 True ou 0.6 é maior que 0.9 True - ",A1 <= B1 or not C1 or D1 > E1 and F1)
respA2 = print("-3.6 é menor igual que -3.59 True ou -0.08 é maior que -0.09 True - ",A2 <= B2 or not C2 or D2 > E2 and F2)
respA3 = print("1.1 é menor igual que 1.1 True ou 3.0 é maior que 3.0 True - ", A3 <= B3 or not C3 or D3 > E3 and F3)
repsA4 = print("7.8 é menor igual que 6.4 True ou 5.0 é maior que -5.0 True - ", A4 <= B4 or not C4 or D4 > E4 and F4)