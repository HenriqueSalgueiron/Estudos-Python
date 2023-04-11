# Crie um programa que leia um nome completo de uma
# pessoa e mostre: a) O nome com todas as letras maiúsculas
# e minúsculas. b) Quantas letras ao todo (sem considerar
#  espaços). c) Quantas letras tem o primeiro nome.

nome = input('Digite seu nome: ').strip()
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome.replace(" ", ""))} letras')
print(f'Seu primeiro nome é {nome.split()[0]} e ele tem {len(nome.split()[0])} letras')
# Poderia ser também print(f'Seu primeiro nome é {nome.split()[0]) e ele tem {nome.find(" ")} letras')

