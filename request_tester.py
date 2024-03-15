import requests
import json

URL_POST = 'http://127.0.0.1:8000/api/students/create/'
URL_GET = 'http://127.0.0.1:8000/api/person/'

URL_AUTH = 'http://127.0.0.1:8000/api/session/auth/'
URL_LOGIN = 'http://127.0.0.1:8000/api/session/login/'

headers = {
    'content-type': 'application/json',
    # 'authorization': 'd1186cqgxh4juo0q4qs5fkncmafcwzi5'
}

# data = {
#     'roll': '12',
#     'name': 'R.Eliodt',
#     'email': 'eliodt@gmail.com',
#     'mark': 50,
#     'details': 'Detail of Eliodt',
#     }

data = {
        "username": "user2",
        "password": "123456sR"
    }

data = json.dumps(data)

# response = requests.post(url=URL_POST, data=data, headers=headers)
response =  requests.post(url=URL_LOGIN, data=data, headers=headers)
print(response.json())