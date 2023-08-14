"""
Flag (Bandeira) - Marcar um local
None = Nao valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""


condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Verdadeiro')
else:
    print('Falso')


if passou_no_if is not None:
    print('Passou no if')
else:
    print('Não passou no if')
