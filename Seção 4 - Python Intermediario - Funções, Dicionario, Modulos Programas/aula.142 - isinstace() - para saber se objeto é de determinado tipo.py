'''

>> isinstace() - para saber se objeto é de determinado tipo

'''

lista = [
    'a', # string 
    1,   # int
    1.1, #float
    True,# bool 
    [0, 1, 2], #list
    (1, 2),    #tupla
    {0, 1},    #set  
    {'nome': 'Luiz'}, # dicionario
]

for item in lista:
    if isinstance(item, str):
        item = item.upper()
        print(item)