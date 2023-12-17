import requests
import json
from typing import Dict, Union, List

class WeatherAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city: str) -> Dict[str, Union[str, int, float]]:
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'  # Запрашиваем данные в метрической системе
        }

        response = requests.get(self.base_url, params=params)

        if response.status_code == 200:
            data = json.loads(response.text)
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']

            return {
                'temperature': temperature,
                'humidity': humidity,
                'wind_speed': wind_speed
            }
        else:
            print(f"Не удалось получить данные о погоде для {city}")
            return {}

    def show_weather(self, city: str) -> None:
        weather_data = self.get_weather(city)
        if weather_data:
            print(f"Температура в {city}: {weather_data['temperature']}°C, влажность: {weather_data['humidity']}%, скорость ветра: {weather_data['wind_speed']} м/с")

class WeatherForecast(WeatherAPI):
    def get_forecast(self, city: str) -> List[Dict[str, Union[str, int, float]]]:
        base_url = "https://api.openweathermap.org/data/2.5/forecast"
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'  # Запрашиваем данные в метрической системе
        }

        response = requests.get(base_url, params=params)

        forecast_data = []
        if response.status_code == 200:
            data = json.loads(response.text)
            for entry in data['list']:
                date = entry['dt_txt']
                temperature = entry['main']['temp']
                humidity = entry['main']['humidity']
                wind_speed = entry['wind']['speed']

                forecast_data.append({
                    'date': date,
                    'temperature': temperature,
                    'humidity': humidity,
                    'wind_speed': wind_speed
                })
        else:
            print(f"Не удалось получить прогноз погоды для {city}")

        return forecast_data

# Пример использования
api = WeatherAPI(api_key='c871c4515f87f048e9db3cfc61351cc5')
api.show_weather('Kyiv')

forecast = WeatherForecast(api_key='c871c4515f87f048e9db3cfc61351cc5')
for day in forecast.get_forecast('Kyiv'):
    print(day)