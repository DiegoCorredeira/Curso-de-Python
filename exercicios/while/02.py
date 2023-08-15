# Crie um programa que solicite ao usuário que insira números inteiros até que ele digite um número negativo.
# Em seguida, exiba a soma de todos os números inseridos.


soma = 0
numeros = []

while True:
    numero = int(input("Digite um número inteiro: "))
    if numero < 0:
        break
    numeros.append(numero)
    soma += numero
print(f"A soma dos números digitados é {soma}")
