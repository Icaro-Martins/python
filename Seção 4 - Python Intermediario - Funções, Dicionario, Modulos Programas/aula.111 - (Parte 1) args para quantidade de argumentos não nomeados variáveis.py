"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)

"""
#Lembre-se de desempacotamento

def soma(*args):
    
    print(*args,type(args))

    total = 0
    for numero in args:
        total += numero
    return total    


totalsoma = soma(1,2,3,4,5,6)   

print(totalsoma)

print(sum((1,2,3,4,5,6)))