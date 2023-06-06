
import copy

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

d2 =  d1.copy() #copia raza, é quando o copy, não acessa as parte onde existem os arrays ou listas 
d3 = copy.deepcopy(d1)# ele copya tudo, tudo que esta no array, lista, todos os subniveis

d2['nome'] = 'Tamiris'

