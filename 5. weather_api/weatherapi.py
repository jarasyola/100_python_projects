import requests

api_key = "d020b86b52c14816b5c757faf833e941"

api_url = "https://api.openweathermap.org/data/2.5/weather"

city = input ("Write your city:")

response = requests.get (
    url = api_url,
    params = {
        "q" : city,
        "appid" : api_key,
        "units" : "metric",
    }
)

weather_data = response.json()
print("The current temperature of ",city," is ", weather_data['main']['temp'], "°C")