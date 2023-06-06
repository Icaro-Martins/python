"""
>>>>> Calculo do primeiro digito do CPF <<<<<

CPF: 413.634.638-70

Colete a soma dos 9 primeiros digitos do CPF
multiplicado cada um dos valores por uma
contagem regressiva começando de 10

Ex.: 413.634.638-70 (413634638)

10
4


"""

import re
import sys
import random


nove_digitos = ''

if nove_digitos in range(9):
    nove_digitos += str(random.randint(0,9))




# >>>>>>>>>>>>>>>>>>>> VALIDAÇÂO DE CAMPO DE USUÀRIO <<<<<<<<<<<<<<<<<<<<<<<<<<
entrada = input('Qual seu CPF: ')

cpf_enviado_pelo_usuario = re.sub(
    r'[^0-9]',# subistitiu tudo de 0 a 9 que não seja (^) um numero, (^ -> é um sinal de negação)
    '',
    entrada
)

entrada_e_sequencia = entrada == entrada[0] * len(entrada)

if entrada_e_sequencia:
    print(f'Você enviou dados squenciais, {entrada}')
    sys.exit()

nove_digitos = cpf_enviado_pelo_usuario[:9]
contador_regressivo_1 = 10
resultado_digito_1 = 0
for digito_1 in nove_digitos:
    resultado_digito_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -=1

digito_1 = (resultado_digito_1 * 10) % 11

digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1

digito_2 = (resultado_digito_2 * 10) % 11    
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

#>>>>>>>>> CPF GERADO

print(cpf_gerado_pelo_calculo)

# >>>>>>>> VAIDA O CPF
if cpf_enviado_pelo_usuario == cpf_gerado_pelo_calculo:
    print(f'{cpf_enviado_pelo_usuario} é valido!')
else:
    print('cpf invalido')
