import calendar

ano = '2021'
mes = '01'

primeirodia, qtddia = calendar.monthrange(int(ano),int(mes))

print(primeirodia, qtddia)

data_inicial = f"{ano}-{mes}-1"
data_pos = f"{ano}-{mes}-{qtddia}"


print(data_inicial)
print(data_pos)