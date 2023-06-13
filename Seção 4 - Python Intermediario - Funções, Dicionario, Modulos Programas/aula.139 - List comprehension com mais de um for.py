import pprint

def impressao(value):
    pprint.pprint(value)

lista = []

for y in range(5):
    for x in range(3):
        lista.append((y,x))        

# Utilizando List comprehension
lista_com = [
    (x,y) 
    for x in range(3)
    for y in range(3)
]

impressao(lista_com)
