# Testes Python 
#
# Github : matheusLeaao  <https://github.com/matheusLeaao>
# @author Matheus Leão <mathegiov@hotmail.com>

"""Faça um programa que receba
duas notas digitadas pelo usuário. 
Se a nota for maior ou igual a cinco, 
escreva aprovado, se for maior que três mas menor
que cinco, escreva reprovado, senão = reprovado."""

cont = 1

print("Digite a "+str(cont)+"ª nota")
nota1 = input()
cont+=cont

print("Digite a "+str(cont)+"ª nota")
nota2 = input()

media = (float(nota1)+float(nota2))/2
print("Sua média é: " + str(media))


if media >= 5:
    print("Aprovado! :)")
elif (media >= 3) and (media <5):
    print("Exame! :s")
else:
    print("Reprovado! :(")
