d1 = {
    'nome': 'Icaro',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereco': [
        {'rua':'tal tal','numeor': True},
        {'rua': 'outra tal', 'numero': 321}
    ]
}


print(d1.get('nome','Nome não existe'))
print()