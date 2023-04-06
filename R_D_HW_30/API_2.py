import requests
import random
import json


while True:
    city = input("City name:")
    coordinates = "https://geocoding-api.open-meteo.com/v1/search?name="
    response = requests.get(f'{coordinates}{city}')
    response_dict = json.loads(response.text)
    city_latitude = round(response_dict.get('results')[0]['latitude'], 2)
    city_longitude = round(response_dict.get('results')[0]['longitude'], 2)
    timezone = "Europe/Moscow"
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={city_latitude}" \
                        f"&longitude={city_longitude}&timezone={timezone}&current_weather=true"

    weather = json.loads(requests.get(weather_url).text)
    temperature = weather.get('current_weather')['temperature']
    windspeed = weather.get('current_weather')['windspeed']
    weathercode = weather.get('current_weather')['weathercode']
    weathercode_dict = weather_dict = {
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

    print(f' Температура: {temperature}, Скорость ветра {windspeed}, {weathercode_dict.get(weathercode)}')


