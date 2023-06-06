"""
Faça uma lsita de compras com listas
O usuário deve ter a possibilidade de 
inserir, apagar e listar valores  de sua lista
Não permitir  que o programa  quebre com 
erros de indices inexistentesna lista.
"""
import os

lista_compas = []

while True:
    print(">>>>>>> SELECIONE UMA OPÇÃO <<<<<<<") 
    opcao = input("[i]nserir | [r]emover | [l]istar: ").lower()
    
    if opcao == "i":
        os.system('cls')
        item = input("Novo Item: ")
        lista_compas.append(item)
    
    elif opcao == "r":
        os.system('cls')
        rmv_item = int(input('Remover Item: '))
        
        try:
            print(f"{lista_compas[rmv_item]}, foi removido da lista de compras.")
            del lista_compas[rmv_item]
        except:
            print('Esse indice não existe!')
            os.system('cls')

    elif opcao == "l":
        os.system('cls')
        if len(lista_compas) == 0:
            print('Sua lista esta vazia!')

        os.system('cls')    

        print("Lista de Compras:") 

        for indice, lis_item in enumerate(lista_compas):
            print(f"\t{indice} - {lis_item}")
    else:
        os.system('cls')
        print('Essa opção não existe!')
                






