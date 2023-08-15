# Crie um programa em que o computador escolha um número aleatório entre 1 e 100, e o usuário precisa adivinhar qual é o número.
# O programa deve fornecer dicas se o número fornecido pelo usuário é maior ou menor que o número escolhido.

import random


random_number = random.randint(1, 100)
palpite = 0
tentativas = 0

while palpite != random_number:
    palpite = int(input("Digite um número: "))
    tentativas += 1
    if palpite > random_number:
        print("O número é menor.")
    elif palpite < random_number:
        print("O número é maior.")
    else:
        print("Você acertou!")
        print(f"Você precisou de {tentativas} tentativas para acertar.")
