import requests
from pprint import pprint

city = input("Enter your city : ")

url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=279376c7a8c24525d2d67c6161858fa8".format(
    city
)

res = requests.get(url)

data = res.json()

temp = data["main"]["temp"]
wind_speed = data["wind"]["speed"]

latitude = data["coord"]["lat"]
longitude = data["coord"]["lon"]

description = data["weather"][0]["description"]

print("Temperature : {} degree celcius".format(temp))
print("Wind Speed : {} m/s".format(wind_speed))
print("Latitude : {}".format(latitude))
print("Longitude : {}".format(longitude))
print("Description : {}".format(description))
