lista = []

for numero in range(10):
    lista.append(numero)

print(lista)

# Tudo o que foi feito acima, esta resumido em apenas 1(UMA) linha
new_list = [numero * 2 for numero in range(10)]
print("new_list ", new_list)