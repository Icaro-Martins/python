
perguntas = [
    {
        "Pergunta" : "Quanto é 2 + 2?",
        "Opções" : ["1","3","4","5"],
        "Resposta" : "4"
    },
        {
        "Pergunta" : "Quanto é  5 * 5?",
        "Opções" : ["25","55","10","51"],
        "Resposta" : "25"
    },
        {
        "Pergunta":"Quanto é 10 / 2:",
        "Opções": ["4","5","2","1"],
        "Resposta": "5"
    }
]

acertos = 0
erros = 0

def forma1():
    print(perguntas[0]['Pergunta'])

    print(f"""
    Opções:
        1) {perguntas[0]["Opções"][0]}
        2) {perguntas[0]['Opções'][1]}
        3) {perguntas[0]["Opções"][2]}
        4) {perguntas[0]["Opções"][3]}
    """)

    opcao = input('Escolha uma Opção: ')
    print(opcao)

    if opcao == '3':
        print('Acertou!')
        acertos += 1
    else:
        print('Errou!')
        erros += 1

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    print(perguntas[1]['Pergunta'])

    print(f"""
    Opções:
        1) {perguntas[1]["Opções"][0]}
        2) {perguntas[1]['Opções'][1]}
        3) {perguntas[1]["Opções"][2]}
        4) {perguntas[1]["Opções"][3]}
    """)

    opcao = input('Escolha uma Opção: ')
    print(opcao)

    if opcao == '1':
        print('Acertou!')
        acertos += 1
    else:
        print('Errou!')
        erros += 1

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    print(perguntas[2]['Pergunta'])

    print(f"""
    Opções:
        1) {perguntas[2]["Opções"][0]}
        2) {perguntas[2]['Opções'][1]}
        3) {perguntas[2]["Opções"][2]}
        4) {perguntas[2]["Opções"][3]}
    """)

    opcao = input('Escolha uma Opção: ')
    print(opcao)

    if opcao == '2':
        print('Acertou!')
        acertos += 1
    else:
        print('Errou!')
        erros += 1

    print("Acertos ", acertos)
    print("Erros ", erros)


def forma2():

    acertos = 0
    erros = 0

    for pergunta in perguntas:
        print('Pergunta: ', pergunta['Pergunta'])
        print()

        opcoes = pergunta["Opções"]

        for i, opcao in enumerate(opcoes):
            print(f'{i})', opcao)            
            
        print()

        escolha = input('Escolha uma opção: ')

        acertou = False
        escolha_int = None
        qtd_opcoes = len(opcoes)

        if escolha.isdigit():
            escolha_int = int(escolha)

        if escolha_int is not None:
            if escolha_int >= 0 and escolha_int <= qtd_opcoes:
                if opcoes[escolha_int] == pergunta['Resposta']:
    
                    acertou = True

        print()    
        if acertou:
            acertos += 1
            print('Acertou')
        else:
            erros += 1
            print('Errou')

        

forma2()