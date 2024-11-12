# weather.py

import requests
import json

def get_weather(city, api_key):
    """
    Get the current weather for a given city.

    Args:
        city (str): The city for which to get the weather.
        api_key (str): The API key for the OpenWeatherMap API.

    Returns:
        dict: A dictionary containing the current weather data.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Use metric units (Celsius, etc.)
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print(f"Error: {response.status_code}")
        return None