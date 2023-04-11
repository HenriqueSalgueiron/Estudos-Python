# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import hypot

print('\nCálculo da hipotenusa!\n')

oposto = float(input('Digite o valor do cateto oposto: '))
adjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = hypot(oposto, adjacente)
# Poderia utilizar também hipotenusa = sqrt(pow(oposto, 2) + pow(adjacente, 2))
# Poderia utilizar também hipotenusa = (oposto ** 2 + adjacente ** 2) ** (1/2)

print(f'O valor da hipotenusa do triângulo é {hipotenusa:.2f}')


