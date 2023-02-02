"""
While (Enquanto)
Excuta uma ação enquanto  uma condição  for verdadeira
Loop infinito -> Enquanto o codigo não tem fim
"""

# Primeiro Teste com while
condicao = True

while condicao:
    nome = input('Qual o seu nome?')
    print(f'seu nome é {nome}')

    if nome == 'sair':
        break # Condição para para o while

print('While é um forma de repetição.') #-> Code is unreachable esse codigo numca sera executada

# Segundo Teste com while

while True:
    nome = input('Qual o seu nome?')
    print(f'seu nome é {nome}')

print('While é um forma de repetição.') #-> Code is unreachable esse codigo numca sera executada