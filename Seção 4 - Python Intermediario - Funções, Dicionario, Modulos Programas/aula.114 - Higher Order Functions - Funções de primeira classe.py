"""
Higher Order Funtions
Funções de primeira classe

"""



def saudacao(msg,nome):
    return f'{msg},{nome}'

def executa(funcao, *args):
    return funcao(*args)

print(
    executa(saudacao('Bom Dia', 'Luiz'))
)

print(
    executa(saudacao('Boa Noite', 'Maria'))
)