# Faça um programa que leia um número de 0 a 9999 e mostre na tela
# cada um dos dígitos separados.
1234
numero = float(input('Digite um número de 0 a 9999: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print(f'Unidade: {int(unidade)}')
print(f'Dezena: {int(dezena)}')
print(f'Centena: {int(centena)}')
print(f'Milhar: {int(milhar)}')

