import socket
import threading
import requests
from geopy.geocoders import Nominatim
import time
import json




server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
port = 12345
server_socket.bind((host, port))
print(f'Сервер запущен по адресу {host}, порту {port}')
server_socket.listen(5)

def get_location_coordinates(word):
    locator = Nominatim(user_agent='myGeocoder')
    location = locator.geocode(word)
    if location is None:
        return None
    print(location.latitude)
    print(location.longitude)
    return (location.latitude, location.longitude)

def handle_client(client_socket, client_address):
    print(f'Подключился клиент: {client_address}')
    message = 'Добро пожаловать! Вы подключены к серверу с погодой. Введите название своего города: '
    client_socket.send(message.encode())
    while True:
        client_message = client_socket.recv(1024).decode()
        if not client_message:
            print(f'Клиент {client_address} отключился')
            client_socket.close()
            break
        words = client_message.strip().lower()
        location = get_location_coordinates(words)
        if location is None:
            message = f'Не удалось определить координаты города {words.title()}. Попробуйте еще раз. '
            client_socket.send(message.encode())
            continue
        API_KEY = '1f5328950f5e7da6800abb0c98e54dab'
        part = 'daily'
        url = f'https://api.openweathermap.org/data/3.0/onecall?lat={location[0]}&lon={location[1]}&exclude={part}&appid={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            date = data['daily'][0]['dt']
            temp_min = data['daily'][0]['temp']['min']
            temp_max = data['daily'][0]['temp']['max']
            message = f'Погода в {words.title()} на {time.strftime("%d-%m-%Y", time.localtime(date))}:\nМинимальная температура: {temp_min} градусов\nМаксимальная температура: {temp_max} градусов\n'
            client_socket.send(message.encode())
        else:
            message = f'Не удалось получить данные о погоде в городе {words.title()}. Попробуйте еще раз. '
            client_socket.send(message.encode())
    client_socket.close()


while True:
    client_socket, client_address = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()