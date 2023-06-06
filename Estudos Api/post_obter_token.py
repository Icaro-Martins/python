import requests


url = 'http://127.0.0.1:3001/token'

user_data = {
    "password": "teste001",
    "email": "email@hotmail.com"
}

response = requests.post(url=url, json=user_data)

if response.status_code >=200 and response.status_code <= 200:
    print(response.status_code)
    print(response.reason)

    token = response.json()['token']
    
    with open('token.txt','w') as file:
        file.write(token)

else:
    print(response.status_code)
    print(response.reason)
    print(response.json())