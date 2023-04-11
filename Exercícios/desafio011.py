#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinra pinta uma área de 2 metros quadrados

largura = float(input('Digite a largura de sua parede: '))
altura = float(input('Digite a altura de sua parede: '))
area = largura * altura
tinta = area / 2

print(f'Sua parede possui {area} metros quadrados')
print(f'Para pintá-la, serão necessários {tinta} litros de tinta')
