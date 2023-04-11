# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente

import math

angulo = float(input('Digite um ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'\nO Seno de {angulo} é {seno:.2f}')
print(f'O Cosseno de {angulo} é {cosseno:.2f}')
print(f'A Tangente de {angulo} é {tangente:.2f}')
