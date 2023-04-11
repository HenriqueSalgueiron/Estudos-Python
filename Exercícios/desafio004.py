variavel = (input('Digite algo: '))
print('Este texto é do tipo primitivo', type(variavel))
print('Este texto é númérico?', variavel.isnumeric())
print('Este texto é alfabético?', variavel.isalpha())
print('Este texto está em caixa alta?', variavel.isupper())
print('Este texto está em caixa baixa?', variavel.islower())
print('Este texto é alfanumérico?', variavel.isalnum())
print('Este texto contém apenas espaços?', variavel.isspace())
print('Este texto contém números do tipo ascchi', variavel.isascii())
print('Este texto contém números entre 0 e 9?', variavel.isdecimal())
print('Este texto contém apenas dígitos?', variavel.isdigit())
print('Este texto é um título? ', variavel.istitle())  # Apenas a primeira letra de cada palavra maiúscula
print('Este texto é um identificador?', variavel.isidentifier())  # A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.
print('Este texto é printável?', variavel.isprintable())

