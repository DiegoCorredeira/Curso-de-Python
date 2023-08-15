# Escreva um programa que imprima um triângulo numérico como o exemplo abaixo, usando loops while aninhados:


i = 1
# enquanto i for menor ou igual a 5
while i <= 5:
    # j recebe 1
    j = 1
    # enquanto j for menor ou igual a i
    while j <= i:
        # imprima j
        print(i, end='')
        # j recebe j + 1
        j += 1
    # imprima uma linha em branco
    print()
    # i recebe i + 1
    i += 1
