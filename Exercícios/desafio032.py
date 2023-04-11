# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date

ano = float(input('Digite o ano. Caso queira o ano atual, digite 0: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: # Para um ano que é divisível por 100 ser bissexto, ele tem de ser divisível
                                                      # também por 400
    print(f'O ano {int(ano)} é bissexto')
else:
    print(f'O ano {int(ano)} não é bissexto')