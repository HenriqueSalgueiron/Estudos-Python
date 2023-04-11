# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela
# aparece a primeira vez e em que posição ela aparece a última vez.

frase = input('Escreva uma frase: ').strip().upper()
print(f'A letra A aparece {frase.count("A")} vezes na frase')
print(f'A letra A aparece a primeira vez na posição {frase.find("A")}')
print(f'A letra A aparece a última vez na posição {len(frase) - 1 - frase[::-1].find("A")}')
#jeito mais correto: print(f'A letra A aparece a última vez a posição {frase.rfind("A")}')

