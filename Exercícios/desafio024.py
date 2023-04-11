# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = input('Digite o nome da cidade: ')
verificação = (cidade.split())[0]
print(f'A cidade começa com "SANTO"?: {"SANTO" in verificação.upper()}')
