##### Calculadora com While ####

while True:

    numero_1 = input('Digite o primeiro numero: ')
    numero_2 = input('Digite o segundo numero: ')
    operador = input('Digite o Operador, [+ | - | * | / ]: ')

    numeros_validos = None #flag
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True # Flag usada para checar se os numeros são validos
    except:
        numeros_validos = None
    
    if numeros_validos is None:
        print('Um ou ambos dos numeros não são validos!')
        continue # se os numeros foram None, apartir dessa etapa ele volta do começo!
    
    operadores_permitidos = '+-*/'
    if operador not in operadores_permitidos:
        print('Operador não permitido!')
        continue
    if len(operador) > 1:
        print('Digite Apenas um Operador!')
        continue


    print('Realizando sua conta confira o resultado abaixo: ')    
    if operador == '+':
        print(f'{num_1_float} + {num_2_float} = ', num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float} = ', num_1_float - num_2_float)
    elif operador == '/':
        print(f'{num_1_float} / {num_2_float} = ', num_1_float / num_2_float)
    elif operador == '*':
        print(f'{num_1_float} * {num_2_float} = ', num_1_float * num_2_float)
    else:
        print('Isso numca deveria acontecer!')

    sair = input('Quer sair? [s]im:' ).lower().startswith('s')

    if sair is True:
        break