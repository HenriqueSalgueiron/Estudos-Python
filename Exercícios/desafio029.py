#Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
# que ele foi multado. A multa vai custar R$7,00 por cada
# Km acima do limite.

velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    multa = 7 * (velocidade - 80 )
    print(f'Você foi multado no valor de R${multa:.2f}!')
print('Tenha um bom dia! Dirija com segurança!')
