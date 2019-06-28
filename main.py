'''

                            Online Python Interpreter.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

# -*- coding:UTF-8 -*- #código de linguagem local, definir acentos nas palavras

print("Entre com o seu nome: ")
nome = input()

#concatenação padrão
print("Qual a sua idade, Sr. "+nome+"?")
idade = input()

cont = 1 

print("Insira o "+str(cont)+"º número")
num1 = int(input())
cont+=cont

print("Insira o "+str(cont)+"º número")
num2 = int(input())

#soma padrão
resultado = num1 + num2

#concatenação realizada(+), no python é necessário converter a variavel
print("Esse é o resultado de "+str(num1)+ "+" +str(num2)+" é: "+str(resultado))

#testando colocar o resultado direto
print(resultado)


