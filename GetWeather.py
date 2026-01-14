import requests
from dotenv import load_dotenv  
import os
import json
with open('icons.json', 'r',encoding="utf8") as file:
    emojiWeather = json.load(file)
load_dotenv()  
openweather_api_key = os.getenv('OPENWEATHERKEY')
def getWeatherString():
    # print(f"OpenWeather API Key: {openweather_api_key}") // For Debug Purposes Only
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    city = os.getenv('CITY')
    complete_url = f"{base_url}?q={city}&appid={openweather_api_key}&units=metric"
    response = requests.get(complete_url)
    weather_data = response.json()
    # print(weather_data)

    temperature = weather_data['main']['temp']
    feels_like = weather_data['main']['feels_like']
    humidity = weather_data['main']['humidity']
    tempMin = weather_data['main']['temp_max']
    tempMax = weather_data['main']['temp_min']
    weather_description = weather_data['weather'][0]['description']
    weather_icon = weather_data['weather'][0]['icon']
    # print(weather_icon)   #Testing
    # print(weather_description) #Testing

    # sentence_weather = weather_description + ", with a temperature of " + str(temperature) + "°C. Feels like is " + str(feels_like), "°C, with a Minimum temperature of " + str(tempMin) + "°C, and a Maximum temperature of " + str(tempMax) + "°C. Humidity is " + str(humidity) + "%."
    # ^ above returns the sentence with brackets around them for some reason
    # print(emojiWeather[weather_icon])
    # ^^ Testing to see if the json icon database works
    weather_message = (
        f" {weather_description.capitalize()} {emojiWeather[weather_icon]}\n"
        f"Temp: {temperature}°C (Feels: {feels_like}°C)\n"
        f"Lo/Hi: {tempMin}°C - {tempMax}°C\n"
        f"Humidity: {humidity}%"
    )
    return weather_message

getWeatherString()