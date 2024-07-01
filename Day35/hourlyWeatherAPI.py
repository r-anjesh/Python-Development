import os

import requests

OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
parameter = {
    "lat":"25.438929",
    "lon":"86.671425",
    "appid" : os.getenv("API_KEY")
}

response = requests.get(OWM_endpoint, params=parameter)
forecast = response.json()
print(forecast)