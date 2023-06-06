'''
Operadores ternario (condicional de uma linha)
<vazio> if <condição> else <outro valor>

'''

condicao = 10 == 10

variavel = 'Valor' if condicao else 'outro valor'
print(variavel)

digito = 9
novo_valor = digito if digito <= 9 else 0
print(novo_valor)

novo_valor = 0 if digito > 9 else digito
print(novo_valor)

print('Valor' if True else 'Outro Valor' if False else 'Fim')