"""
Valores padrão  para parametros
Ao definir uma função, os  parametros podem
ter valores padão. Caso o valor não seja
enviado para o paramtros, os padão será
usado.

"""


def soma(x, y, z):
    if z is not None:
        print(f'{x=} {y=} {z=} ', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)


#soma(1,2)
#soma(4,5)
soma(3,5,6)
soma(x=3,y=5,z=6)