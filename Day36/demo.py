import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "4B0WP1H6NP2XU2ZA"
NEWS_API_KEY = "238de636843c431f861e9b28dfaf48e2"
ACCOUNT_SID = "AC7040ee5722e907c65c2d3a9f0db911d9"
AUTH_TOKEN = "c04e31caf1d87cbe3c49244230cd4089"

parameter = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

response = requests.get(url="https://www.alphavantage.co/query", params=parameter)
data = response.json()
print(data)