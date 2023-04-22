lista = [10,20,30,40,50,60,70,80,100]
print('Lista Inicial:', lista)
lista.append(110)
print('Add 110 na lista')
lista.append(120)
print('Add 120 na lista')
print('Append de dados', lista)
lista[5] = 51
print('Alterando dado da posição')
del lista[-2]
print('Deletando numero 80')
print(lista)
lista.pop()
ultimo_valor = lista.pop(3)
print(lista, 'Removido,', ultimo_valor)