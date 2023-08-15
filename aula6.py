qtd_linhas = 5
qtd_colunas = 5

linha = 1

# A cada iteração do while externo, o while interno é executado 5 vezes
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f"Linha={linha}, Coluna={coluna}")
        coluna += 1
    print()
    linha += 1
