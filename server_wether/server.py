import socket
import threading
import requests

api_key = '04c9a2fe64449b0348eb38d5920909f2'
url_base = 'https://api.openweathermap.org/data/2.5/'

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 1010

server_socket.bind((host, port))
print(f'Server is running on {host}:{port}')

server_socket.listen(5)

welcome_message = 'Welcome! You are connected to the weather server.\n'


def handle_client(client_socket, client_address):
    print(f'Client connected: {client_address}')
    client_socket.send(welcome_message.encode())

    while True:
        client_message = client_socket.recv(1024).decode()

        if not client_message:
            print('Client disconnected: ', client_address)
            break

        def weather_forecast(q: str = 'Barnaul, RU', appid: str = api_key, units: str = 'metric'):
            response = requests.get(url_base + 'forecast', params={'q': q, 'appid': appid, 'units': units}).json()

            week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            if response["cod"] == '404':
                print("City not found.")
                return "City not found."
            else:
                weather_info = ''
                for i in range(7):
                    day = response['list'][i]
                    date = day['dt_txt']
                    weather = day['weather'][0]['description']
                    avg_temp = round((day['main']['temp_max'] + day['main']['temp_min']) / 2)
                    max_temp = day['main']['temp_max']
                    min_temp = day['main']['temp_min']
                    humidity = day["main"]["humidity"]
                    wind_speed = day["wind"]["speed"]
                    weather_info += f'Date: {date}\n' \
                                    f'\nDay of the week: {week_days[i]}\n' \
                                    f'Description: {weather}\n' \
                                    f'Max temperature: {max_temp}\n' \
                                    f'Min temperature: {min_temp}\n' \
                                    f'Average temperature: {avg_temp}\n' \
                                    f'Humidity %: {humidity}\n' \
                                    f'Wind speed (m/s): {wind_speed}\n' \
                                    f'______________________________________\n'
                return weather_info

        weather_data = weather_forecast(client_message.strip())
        client_socket.send(weather_data.encode())

    client_socket.close()


while True:
    client_socket, client_address = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
