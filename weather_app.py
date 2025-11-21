import requests

def get_weather(city):
    API_KEY = "YOUR_API_KEY"   # Replace with your real API key
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()

        city_name = data["name"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather_condition = data["weather"][0]["description"].title()

        print("\n===== Weather Report =====")
        print(f"City: {city_name}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {weather_condition}")
        print("==========================\n")

    else:
        print("Error: City not found or invalid API key.")

city = input("Enter city name: ")
get_weather(city)
