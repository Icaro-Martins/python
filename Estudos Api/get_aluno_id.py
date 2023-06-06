import requests
from get_token import token


url = 'http://127.0.0.1:3001/alunos/3'


headers = {
    #'Authorization': token
}

aluno_data = {
    #"nome": "João",
    #"sobrenome": "Moreira" ,
    #"email": "teste@gmail.com",
    #"idade": "21",
    #"peso": "70.00",
    #"altura": "1.75"

}

response = requests.post(url=url, json=aluno_data, headers=headers)

if response.status_code >= 200 and response.status_code <= 299:
    print(response.status_code)
    print(response.reason)

    response_data = response.json()

    for aluno in response_data:
      print(aluno['nome'])  


else:
    print(response.status_code)
    print(response.reason)    