# Using requests module to get data from API, using JSON
import requests

# Insert your weatherapi API key here
api_key = "123456"
city = "Austin"

url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
weather_data = requests.get(url).json()
location = weather_data["location"]["name"]
temperature = weather_data["current"]["temp_c"]
condition = weather_data["current"]["condition"]["text"]
is_day = weather_data.get("current").get("is_day")

print(f"Weather in {location}: {temperature} C. \nIt is {"night" if is_day == 0 else "day"} and the weather condition is {condition}")