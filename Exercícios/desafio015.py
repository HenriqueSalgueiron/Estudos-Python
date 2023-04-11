# Escreva um programa que pergunte a quantiade de Km percorridos por um carro alugado e a quantidade de dias pelos quais
# ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por Km rodado


dias = int(input('Por quantos dias você alugou o carro? '))
distancia = float(input('Quantos Km você rodou com o carro? '))

print(f'O preço a pagar é: R${dias*60+0.15*distancia:.2f}')
