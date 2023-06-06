import requests
from get_token import token


url = 'http://127.0.0.1:3001/alunos/3'# -->> Apontar o ID de qual aluno eu quero atualizar


headers = {
    'Authorization': token
}

aluno_data = {
    "nome": "Predo", #->> Atualizando somento o nome
    #"sobrenome": "Moreira" ,
    #"email": "teste@gmail.com",
    #"idade": "21",
    #"peso": "70.00",
    #"altura": "1.75"

}

response = requests.put(url=url, json=aluno_data, headers=headers)# --> Ajustar colocando o PUT() para atualizar

if response.status_code >= 200 and response.status_code <= 299:
    print(response.status_code)
    print(response.reason)

else:
    print(response.status_code)
    print(response.reason)    