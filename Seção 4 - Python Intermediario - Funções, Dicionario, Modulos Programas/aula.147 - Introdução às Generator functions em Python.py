# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

def generator(n=0):
    yield 1 # Toda função geradora em python utiliza yield, PAUSA A EXECUÇÂO DA FUNÇÃO.
    print('CONTINUANDO....')
    yield 2
    return 'ACABOU !!'

gen = generator(n=0)

#for n in gen:
#    print(n)


# ---------------------------------------------


def generator2(n=0, maximum=10):
    while True:
        yield n
        n+=1

        if n >= maximum:
            return

gen2 = generator2(maximum=100)

for n in gen2:
    print(n)

