
pessoa = {
    'nome': 'Icaro',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereco': [
        {'rua':'tal tal','numeor': True},
        {'rua': 'outra tal', 'numero': 321}
    ]
}

#posso usar essas duas formas para saber a quantidade de chaves que tem no meu dict, porem a mais comum pe len
print(len(pessoa))
print(pessoa.__len__())



print('Keys ', list(pessoa.keys()))
for chave in pessoa.keys():
    print(chave)


print('Values ', list(pessoa.values()))
for valor in pessoa.values():
    print(valor)

print('Items: ', pessoa.items())
for items in pessoa.items():
    print(items)

print('setdefault: ', pessoa.setdefault('idade', 0))
