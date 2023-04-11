# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira
from math import trunc

numero = float(input('Digite um número real qualquer: '))

print(f'A porção inteira de {numero} é {trunc(numero)}')

#Poderia também ter sido feito usando {int(numero)} ou {numero:.0f}



