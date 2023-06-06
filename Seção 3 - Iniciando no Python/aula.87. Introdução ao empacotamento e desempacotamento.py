''' Introdução aop desempacotamento + tuplas '''


lista = ['Icaro', 'Daniel', 'Douglas']

#---- Criando varieaveis apertir dos valores da lista ---

print("------------- 1° Forma -------------")
nome1, nome2, nome3 = lista
print(nome1, nome2, nome3)

print("------------- 2° Forma -------------")
nome1, nome2, nome3 = lista = [ 'Icaro', 'Daniel', 'Douglas']
print(nome1, nome2, nome3)


print("------------- 3° Forma -------------")
nome1, *resto = [ 'Icaro', 'Daniel', 'Douglas', 'Van', 'Renilson']
print(nome1, resto)
