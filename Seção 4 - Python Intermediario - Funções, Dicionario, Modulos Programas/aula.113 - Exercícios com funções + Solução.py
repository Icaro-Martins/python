"""

Exercicios com Funções

Crie uma função que multiplica todos os argumentos não nomeados recebidos
Retorne o total para um variavel e mostre o valor da variavel.

Crie um função fala se um numero é par ou impar.
Retorne se o numero é par ou impar

"""


def _multiplca(*args):

    resultado = 1

    for valor in args:
       resultado *= valor
       

    return resultado


def _parImpar(x):
    resultado = x % 2 == 0

    if resultado:
        return f'{resultado}, é par'
    return f'{resultado}, é impar'



resultado = _multiplca(1, 2, 3, 4, 5, 6)

print('resultado ', resultado)
print(_parImpar(100))

