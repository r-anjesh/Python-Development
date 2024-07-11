import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "*********"
NEWS_API_KEY = "*************"
ACCOUNT_SID = "********"
AUTH_TOKEN = "**********"

parameter = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

response = requests.get(url="https://www.alphavantage.co/query", params=parameter)
data = response.json()
print(data)