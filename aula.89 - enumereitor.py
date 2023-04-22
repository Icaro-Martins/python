print('Criando a Lista')
lista = [ 'Icaro', 'Daniel', 'Douglas', 'Van', 'Renilson']
print('Lista criada')

print()

print('Enumerando a lista')
lista_enumerada = enumerate(lista)

print()

print(f'Next() > ', next(lista_enumerada))

print()

""" 
>>>> Acessando itens dentro da variavel 'lista_enumerada', 
     após ela ser executada pelo for, ela sera cosumida 
     e os dados seram zerados. <<<<
"""

print()

print('>>>> Inicio For')
for item in lista_enumerada:
    print(item)
print('>>>> Fim For')
print()

print('Usando o enumerate direto no for, sem atribuilo a uma variavle.\n Dessa forma eu posso usala varias vezes no for.')

for item in enumerate(lista):
    print(item)
for item in enumerate(lista):
    print(item)    

for item in enumerate(lista):
    print(item)

for item in enumerate(lista):
    print(item)

for item in enumerate(lista):
    print(item)

print()

print('Caso eu não queira usar o for para acessar os itens dento do enumerator, \n eu posso transformar em uma lsita novamente.')

print("Enumerator transformado em lsita.\n", list(enumerate(lista)))

print()

print('Desenpacotando os dados da tupla.')
for indice, valor in enumerate(lista):
    print(indice,valor)    

print()

print('2º Forma de desenpacotar os valores da tupla')
for item in enumerate(lista):
    indice, valor = item
    print(indice, valor)


