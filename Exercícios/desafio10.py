# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,27

valor = float(input('Digite quanto de dinheiro você tem: '))

print(f'Com R${valor} você poderá comprar US${valor/3.27:.2f}')

