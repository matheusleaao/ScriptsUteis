# Testes Python 
#
# Github : matheusLeaao  <https://github.com/matheusLeaao>
# @author Matheus Leão <mathegiov@hotmail.com>


"""Escreva um programa que receba dois números e um sinal, 
e faça a operação matemática definida pelo sinal."""

cont = 1
print("Entre com o "+str(cont)+"º número")
numUm = float(input())

cont+=cont

print("Entre com o "+str(cont)+"º número")
numDois = float(input())

print("Qual operação deseja que seja feita?")
operacao = input()

if operacao == '*':
    resultado = numUm * numDois
    print("O resultado de "+str(numUm)+" "+operacao+" "+str(numDois)+" é de "+str(resultado)+"")
elif operacao == '/':
    resultado = numUm / numDois
    print("O resultado de "+str(numUm)+" "+operacao+" "+str(numDois)+" é de "+str(resultado)+"")
elif operacao == '+':
    resultado = numUm + numDois
    print("O resultado de "+str(numUm)+" "+operacao+" "+str(numDois)+" é de "+str(resultado)+"")
elif operacao == '-':
    resultado = numUm - numDois
    print("O resultado de "+str(numUm)+" "+operacao+" "+str(numDois)+" é de "+str(resultado)+"")
else:
    print("Operação inválida.")
