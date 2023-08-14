"""
Exercicio: 

Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se o nome e idade forem digitados:
    Exiba: 
        Seu nome é: <nome>
        Seu nome invertido é: <nome invertido>
        Seu nome contém (ou não) espaços
        seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A ultima letra do seu nome é {letra}
Se nada for digitado:
    Exiba:
        "Desculpe, você não digitou nada"

"""

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if nome and idade: 
    print(f"Seu nome é: {nome}")
    print(f"Seu nome invertido é: {nome[::-1]}")
    print(f"Seu nome contém espaços: {' ' in nome}")
    print(f"Seu nome tem {len(nome)} letras")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A ultima letra do seu nome é {nome[-1]}")
else:
    print("Desculpe, você não digitou nada")