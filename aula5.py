""" 
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> loop que não tem fim
while com break -> para o loop
while com continue -> pula a iteração
"""
condicao = True

# while condicao:
#     nome = input("Digite seu nome: ")
#     if nome == "sair":
#         break
#     print(nome)


cont = 0
while cont <= 100:
    cont += 1
    if cont == 6:
        continue
    if cont >= 10 and cont <= 20:
        continue
    print(cont)
    if cont == 40:
        break


