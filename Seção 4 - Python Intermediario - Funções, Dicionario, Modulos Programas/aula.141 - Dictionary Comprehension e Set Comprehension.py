# Dictionary Comprehension e Set Comprehension

produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritorio',
    'IsEmail': True,
    'Email': 'teste@gmail.com'
}

for chave, valor in produto.items():
    ...
    #print(chave, valor)

dc = {
    chave: valor.lower()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
}

print(dc)
