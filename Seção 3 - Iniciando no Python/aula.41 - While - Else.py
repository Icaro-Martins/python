string = 'valorqualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra in " ":
        break

    print(letra)
    i += 1

else:
    print('Não encontrei nenhum espaço na string.')
print('Fora do while!')
