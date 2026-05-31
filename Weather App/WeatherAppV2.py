import requests
import json

cities = []

def load_history():
    global cities
    try:
        with open("cities.json", "r") as f:
            cities = json.load(f)
    except FileNotFoundError:
        cities = []

def save_history():
    with open("cities.json", "w") as f:
        json.dump(cities, f, indent=4)

def search_Weather():
    location = input("Enter your Location : ")

    url = (f"https://geocoding-api.open-meteo.com/v1/search?name={location}&count=1")

    response = requests.get(url)
    data = response.json()

    if "results" not in data:
        print("City not found!")
        return
    
    latitude = data["results"][0]["latitude"]
    longitude = data["results"][0]["longitude"]

    weather_url = (f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true")
    
    weather_response = requests.get(weather_url)

    data = weather_response.json()

    if weather_response.status_code == 200:
        if location.title() not in cities:
            cities.append(location.title())
            save_history()
        
        time = data["current_weather"]["time"]
        temperature = data["current_weather"]["temperature"]
        wind_speed = data["current_weather"]["windspeed"]
        wind_direction = data["current_weather"]["winddirection"]
        weather_code = data["current_weather"]["weathercode"]

        weather_codes = {
        0: "Clear Sky",
        1: "Mainly Clear",
        2: "Partly Cloudy",
        3: "Overcast"
        }

        description = weather_codes.get(weather_code,"Unknown Weather")

        print("\n===== Weather Report =====")
        print(f"Time           : {time}")
        print(f"Temperature    : {temperature}°C")
        print(f"Wind Speed     : {wind_speed} km/h")
        print(f"Wind Direction : {wind_direction}°")
        print(f"Description    : {description}")
    else:
        print("API unavailable")

def view_History():
    if len(cities) == 0:
        print("No Search History!")
        return

    print("\n===== Search History =====")

    for i, city in enumerate(cities, start=1):
        print(f"{i}. {city}")

load_history()
while True:
    print("====Weather App====")
    print("1. Search Weather")
    print("2. View History")
    print("3. Exit")

    try:
        option = int(input("Select One Option : "))
    except ValueError:
        print("Please enter a valid option!")
        continue

    if option == 1:
        search_Weather()
    elif option == 2:
        view_History()
    elif option == 3:
        break
    else:
        print("Invalid Option !!!")