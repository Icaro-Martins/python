import pprint


def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)


produto = [
    {"nome":"p1", "preco": 20, },
    {"nome":"p2", "preco": 10, },
    {"nome":"p3", "preco": 30, }
]


# antes do for é mapeamento, depois do for é filto
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produto
    if produto['preco'] > 10
]

p(novos_produtos)


lsita = [n for n in range(10) if  n < 5]