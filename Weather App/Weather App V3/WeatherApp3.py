from flask import Flask, render_template, request
import requests
app = Flask(__name__)


@app.route("/", methods = ["GET", "POST"])
def weather():
    if request.method == "POST":
        city = request.form["city"]
        location = city
        url = (f"https://geocoding-api.open-meteo.com/v1/search?name={location}&count=1")
        
        response = requests.get(url)
        data = response.json()

        if "results" not in data:
            return "City Not Found"
        
        latitude = data["results"][0]["latitude"]
        longitude = data["results"][0]["longitude"]

        weather_url = (f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true")
        
        weather_response = requests.get(weather_url)

        data = weather_response.json()

        if weather_response.status_code == 200:
            
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

            return render_template("weather.html",location = city, time = time, temperature=temperature, wind_speed = wind_speed, wind_direction = wind_direction, description = description)
        else:
            return "API unavailable"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)