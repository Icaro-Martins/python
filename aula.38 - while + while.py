qtd_colunas = 5
qtd_linhas = 5
count_linhas = 1


while count_linhas <= qtd_linhas:
    count_colunas = 1
    while count_colunas <= qtd_colunas:
        print(f'{count_linhas=}, {count_colunas=}')
        count_colunas += 1
    count_linhas += 1