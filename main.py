import requests
import json
import pyttsx3


engine = pyttsx3.init()
while True:
    city_input = "\nWhat city's temperature would you like to check (enter quit if you want exit): "
    engine.say(city_input)
    engine.runAndWait()
    city = input(city_input)
    if city == "quit":
        break

    url = f'https://api.weatherapi.com/v1/current.json?key=4ee830a205904bbe95f185328243103&q={city}'
    r = requests.get(url)
    weather_data = json.loads(r.text)
    temp = f"The temperature of {city} is {weather_data['current']['temp_c']} °C"
    print(temp)
    engine.say(temp)
    engine.runAndWait()



