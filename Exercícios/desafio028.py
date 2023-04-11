#  Escreva um programa que faça o computador “pensar” em
#  um número inteiro entre 0 e 5 e peça para o usuário
#  tentar descobrir qual foi o número escolhido pelo
#  computador. O programa deverá escrever na tela se o
#  usuário venceu ou perdeu.
import random
import time
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
usuario = int(input('Em que número eu pensei? '))
numero = random.randint(0,5)
print('Analisando...')
time.sleep(2)
if usuario == numero:
    print(f'PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {numero} e não no {usuario}')