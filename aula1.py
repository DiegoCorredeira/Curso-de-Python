"""
    Fatiamento de Strings
    0123456789.............33
    Olá mundo
    -987654321
    Fatiamento [inicio:fim:passo] [::]
    Obs. : a função len() conta a quantidade de caracteres de uma string
"""

variavel = "Olá Mundo!"
print(len(variavel[0:3])) # imprime Olá || 3 caracteres
print(len(variavel[4:9])) # imprime Mundo || 5 caracteres
print(len(variavel[0:9:2])) # imprime OáMno || 5 caracteres
print(len(variavel[5:])) # imprime Mundo! || 5 caracteres