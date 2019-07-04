# -*- coding: utf-8 -*-

# programa que realiza uma equação de primeiro grau

# a2 + bx + c 
# (-b +- sqrt(b2 - 4ac )) / 2 

from math import sqrt #utilizado para importar a raiz quadrada

a = float(input("Digite o valor de 'A': "))
b = float(input("Digite o valor de 'B': "))
c = float(input("Digite o valor de 'C': "))

delta = b**2 - 4*a*c
raizDelta = sqrt(delta)

x1 = (-b + raizDelta)/ (2*a)
x2 = (-b - raizDelta)/ (2*a)

print ("x1 = "+str(x1)+"")
print ("x2 = "+str(x2)+"")