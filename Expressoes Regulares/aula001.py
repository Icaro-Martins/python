import re

string = "Este é um teste de expressões teste regulares."

print(re.search(r'teste', string))
print(re.findall(r'teste', string))
print(re.sub(r'teste','ABCD', string))

regex = re.compile(r'teste')

print(regex.findall(string))
print(regex.search(string))
print(regex.sub('DEF',string))