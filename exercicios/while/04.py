# Crie um programa que imprima a tabela de multiplicação de 1 a 10 usando dois loops

i = 1
# Para cada valor de i, o loop interno é executado 10 vezes
while i <= 10:
    j = 1
    while j <= 10:
        print(f'{i} x {j} = {i * j}')
        j += 1
    i += 1

