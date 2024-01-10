import re

texto = '''
João trouxe   flores para sua mada namorada em 10 de janeiro de 1970,
Mariaera o nome dela.

Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de domingo. Tambem né!
Sendo a boa mineira que é, nunca exuece seu famoso pão de queijo.
Nãoi canso de ouvir a Maria:
"Jooooooooooooãoooooo, o café tá prontinho aqui. Veeemm!"
'''

print(re.findall(r'João|Maria', texto))
print(re.findall(r'João|Maria|f..hos', texto))
print(re.findall(r'[Jj]oão|[Mm]aria',texto))
print(re.findall(r'[a-z]oão|[a-z]aria', texto))
print(re.findall(r'[a-zA-Z0-9]aria|[a-zA-Z0-9]oão',texto))
print(re.findall(r'jOãO|mArIa', texto, flags=re.IGNORECASE))