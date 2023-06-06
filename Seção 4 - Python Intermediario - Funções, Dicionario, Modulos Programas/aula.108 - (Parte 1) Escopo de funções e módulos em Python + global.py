"""
Escopo de função em Python
Escopo significa o local onde aquele codigo pode atingir
Existe o escopo global e local.
O escopo global é o escopo onde todo o codigo é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo loval podem ser alcançados.

"""

x = 1

def escopo():
    global x
    x = 10

    def outro_escopo():

        x=11
        y=2
        print(x,y)

    outro_escopo()     
    print(x)


escopo()
