import requests
from pprint import pprint
_print = pprint

url = 'http://127.0.0.1:3001/users'

user_data = {
    "nome": "icaro martins",
    "password": "teste001",
    "email": "email@hotmail.com"
}

response = requests.post(url=url, json=user_data)

if response.status_code >= 200 and response.status_code <= 299:
    #sucesso
    print('Status Code: ', response.status_code)
    print('Reason: ', response.reason)
    print('Texto: ', response.text)
    print('Json: ', response.json())

else:
    #erros
    print('Status Code: ', response.status_code)
    print('Reason: ', response.reason)
    print('Texto: ', response.text)


