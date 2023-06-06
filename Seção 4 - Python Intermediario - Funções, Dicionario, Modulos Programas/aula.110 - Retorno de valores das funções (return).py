"""
Retorno de valores da função (return)

"""


def soma(x,y):
    if x  > 10:
        return [10,20]
    return x + y

soma1 = soma(2,3)
soma2 = soma(4,5)

print(soma1)
print(soma2)
print(soma(11,55))