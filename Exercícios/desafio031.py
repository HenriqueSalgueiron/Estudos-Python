#Desenvolva um programa que pergunte a distância de uma
#viagem em Km. Calcule o preço da passagem, cobrando
#R$0,50 por Km para viagens de até 200Km e R$0,45 parta
#viagens mais longas.

distancia = float(input('Digite a distância percorrida em viagem: '))
print(f'O valor da passagem será de R${(distancia * 0.5 if distancia <= 200 else distancia * 0.45):.2f}')

''' Outra opção: 

if distancia <= 200:
    print(f'O valor da passagem é R${distancia * 0.5}')
else:
    print(f'O valor da passagem é R${distancia * 0.45}') '''

