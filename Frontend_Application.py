import requests
import json

# URL = 'http://127.0.0.1:8000/serializer/get_student/1'
# URL = 'http://127.0.0.1:8000/serializer/get_all_student/'

# r = requests.get(url = URL)

# data = r.json()

# print(data)

# URL = "http://127.0.0.1:8000/deserializer/create-student/"

# data = {
#     'name': 'Zohan',
#     'roll': 123,
#     'city': 'Karachi'
# }

# json_data = json.dumps(data)

# r = requests.post(url=URL, data=json_data)

# dataa = r.json()

# print(dataa)

URL = "http://127.0.0.1:8000/api-view-app/student-api/"

def get_data(id=None):
    data = {}
    if id is not None:
        data = {
            'id': id
        }
    json_data = json.dumps(data)
    r = requests.get(url = URL, headers = {'content-Type':'application/json'}, data = json_data)
    data = r.json()
    print(data)

get_data(1)

def create_data():
    data = {
        'name': 'error',
        'roll': 211,
        'city': 'Karachi'
        }

    json_data = json.dumps(data)
    r = requests.post(url = URL, headers = {'content-Type':'application/json'}, data = json_data)
    data = r.json()
    print(data)

# create_data()

def update_data():
    data = {
        'id': 1,
        'name': 'Zohan Zafar',
        'city': 'Lahore'
        }

    json_data = json.dumps(data)
    r = requests.put(url = URL, headers = {'content-Type':'application/json'}, data = json_data)
    data = r.json()
    print(data)

# update_data()

def delete_data():
    data = {
        'id': 4
    }
    json_data = json.dumps(data)
    r = requests.delete(url = URL, headers = {'content-Type':'application/json'}, data = json_data)
    data = r.json()
    print(data)

# delete_data()