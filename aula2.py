"""
Introdução ao Try/Except

Try -> tente executar o codigo
Except -> caso de erro, execute isso
"""

numero_str = input('Vou dobrar o numero que voce digitar: ')

try:
    numero_float = float(numero_str)
    print(f'O dobro de {numero_float} é {numero_float * 2})')
except:
    print('Não é um numero inteiro')