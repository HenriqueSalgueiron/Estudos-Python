# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input("Digite seu nome: "))
nomes = nome.split()
print(f'Seu primeiro nome é {nomes[0]}')
print(f'Seu último nome é {nomes[int(len(nomes) - 1)]}')