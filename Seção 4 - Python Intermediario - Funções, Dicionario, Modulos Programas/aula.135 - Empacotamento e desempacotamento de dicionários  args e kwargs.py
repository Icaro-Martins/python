# Empacotamento e desempacotamento de dicionários + *args e **kwargs

a, b = 1, 2
a, b = b, a

pessoa = {
    "nome": "Alice",
    "sobrenome": "souza"
}

dados_pessoa = {
    "idade": 16,
    "altura": 1.60
}





# 2° Formad e extrair MAI DE 1(UM) dicionario (args)
pessoa_completa = {**pessoa, **dados_pessoa}# <<< args

print(pessoa_completa)


# 1° Forma de extrair 1 UM dicionario
#a,b = pessoa.values()

#for chave, valor in pessoa.items():
#    print(chave, valor)

