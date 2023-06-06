contador = 0

while contador < 100:
    contador += 1

    if contador == 6:
        print(f'Não vou mostra o valor {contador}')
        continue

    if contador >= 10 and contador <= 20:
        print(f'Não vou mostra o valor {contador}')
        continue

    print(contador)   

    if contador == 40:
        break 


    