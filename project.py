"""
Script Name: Weather Script

Description:
This script fetches weather data from OpenWeatherMap API for a specified city and displays the current temperature, wind speed, and weather description.

This script also retreives code inspiration using the umanganhuja1 github repo.

Usage:
1. Run the script.
2. Enter the city when prompted.

Dependencies:
- Requests library
- Python 3.x

Author: Bethel Sheferaw
Date: December 16, 2023
"""


import re
import requests


# This function takes a city input and uses a regular expression to validate it. The regular expression checks for a city name with optional leading and trailling spaces. 
def validate_city_input(city_input):
    pattern = re.compile(r"^\s*([A-Za-z\s]+)\s*$")
    match = pattern.match(city_input)
    return match


# Gets city input from the user
city_input = input("Enter your city: ")

# Validates the city input, and checks if the input is valid, if it is it extracts the city name using the group(1) method.
city_match = validate_city_input(city_input)

if city_match:
    # Extract the validated city
    city = city_match.group(1)
    # Use a raw string for the URL to avoid backslashes
    url = rf"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=279376c7a8c24525d2d67c6161858fa8"

    # Make the API request
    res = requests.get(url)
    data = res.json()
#These lines checks if the API request was successful (status code 200) and print vaious weather-related information, such as city name, latitude, longtitude, temperature, wind speed, and weather description.
    if res.status_code == 200:
        print("Weather Data:")
        print(f"City: {city}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
        print(f"Latitude: {data['coord']['lat']}")
        print(f"Longitude: {data['coord']['lon']}")
        print(f"Description: {data['weather'][0]['description']}")

    else:
        #if the api rewuest fails, it then prints an error message containing the error details. 
        print(f"Failed to fetch weather data. Error: {data['message']}")
else:
    #If the city input is not valid it prints an error message. 
    print("Invalid city input. Please enter a valid city name.")
