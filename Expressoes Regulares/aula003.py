# quantificadores 
# * 0 ou n
# + 1 ou n
# ? 0 ou 1
# { } n | min, max

import re

texto = '''
João trouxe   flores para sua mada namorada em 10 de janeiro de 1970,
Mariaera o nome dela.

Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de domingo. Tambem né!
Sendo a boa mineira que é, nunca exuece seu famoso pão de queijo.
Nãoi canso de ouvir a Maria:
"Jooooooooooooãoooooo, o café tá prontinho aqui. Veeemm!"
Joãoooooo
João ama ser amado.
'''

print(re.findall(r'[a-zA-Z]o+ão*', texto))
print(re.findall(r'Jo{1,}ão*', texto))
print(re.findall(r'Jo+ão', texto))
print(re.findall(r'Jo{1,}ão{1,}', texto))
print(re.findall(r'Jo{1,}ão{1,}', texto))
print(re.findall(r'ama[do]{2}', texto))