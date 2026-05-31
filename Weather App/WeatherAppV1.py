import requests

cities = {
    "Vadodara": (22.3072, 73.1812),
    "Mumbai": (19.0760, 72.8777),
    "Delhi": (28.6139, 77.2090),
    "Bangalore": (12.9716, 77.5946)
}

usercity = input("Enter City : ").title()

if usercity not in cities:
    print("City Not Found")
    exit()

lat, lon = cities[usercity]

url = (f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true")

response = requests.get(url)

data = response.json()

if response.status_code == 200:
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
    print(f"City         : {usercity}")
    print(f"Time         : {time}")
    print(f"Temperature  : {temperature}°C")
    print(f"Wind Speed   : {wind_speed} km/h")
    print(f"Wind Dir     : {wind_direction}°")
    print(f"Description  : {description}")
else:
    print("API unavailable")