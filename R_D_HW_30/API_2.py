import requests
import random
import json


weathercode_dict = {
    0: 'Ясное небо',
    1: 'Преимущественно ясно',
    2: 'Частичная облачность',
    3: 'Пасмурно',
    45: 'Туман и иней',
    48: 'Мгла и иней',
    51: 'Морось: слабая интенсивность',
    53: 'Морось: умеренная интенсивность',
    55: 'Морось: сильная интенсивность',
    56: 'Ледяной дождь: слабая интенсивность',
    57: 'Ледяной дождь: сильная интенсивность',
    61: 'Дождь: незначительная интенсивность',
    63: 'Дождь: умеренная интенсивность',
    65: 'Дождь: сильная интенсивность',
    66: 'Ледяной дождь: слабая интенсивность',
    67: 'Ледяной дождь: сильная интенсивность',
    71: 'Снег: незначительная интенсивность',
    73: 'Снег: умеренная интенсивность',
    75: 'Снег: сильная интенсивность',
    77: 'Снежинки',
    80: 'Кратковременный дождь: незначительная интенсивность',
    81: 'Кратковременный дождь: умеренная интенсивность',
    82: 'Кратковременный дождь: сильная интенсивность',
    85: 'Кратковременный снег: незначительная интенсивность',
    86: 'Кратковременный снег: сильная интенсивность',
    95: 'Гроза: незначительная или умеренная',
    96: 'Гроза с легким градом',
    99: 'Гроза с сильным градом'
}


def get_weather_url(latitude, longitude, timezone):
    return f"https://api.open-meteo.com/v1/forecast?latitude={latitude}" \
           f"&longitude={longitude}&timezone={timezone}&current_weather=true"

while True:
    city = input("City name:")
    coordinates = "https://geocoding-api.open-meteo.com/v1/search?name="
    try:
        response_dict = requests.get(f'{coordinates}{city}').json()
        city_latitude = round(response_dict.get('results')[0]['latitude'], 2)
        city_longitude = round(response_dict.get('results')[0]['longitude'], 2)
        timezone = "Europe/Kiev"
        weather_url = get_weather_url(city_latitude, city_longitude, timezone)

        weather = json.loads(requests.get(weather_url).text)
        temperature = weather.get('current_weather')['temperature']
        wind_speed = weather.get('current_weather')['windspeed']
        weather_code = weather.get('current_weather')['weathercode']

        print(f' Температура: {temperature}, Скорость ветра {wind_speed}, {weathercode_dict.get(weather_code)}')
    except (Exception):
        print('No city with that name')















