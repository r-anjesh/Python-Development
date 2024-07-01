import requests
from twilio.rest import Client



STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "********"
NEWS_API_KEY = "***********************"
ACCOUNT_SID = "************************"
AUTH_TOKEN = "*****************"

parameter = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "apikey" : STOCK_API_KEY
}

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get(url="https://www.alphavantage.co/query",params= parameter)

data = response.json()['Time Series (Daily)']

data_list = [value for (key,value) in data.items()]
yesterday_closing_price = data_list[0]["4. close"]

day_before_yesterday_closing_price = data_list[1]['4. close']

difference = abs(float(day_before_yesterday_closing_price) - float(yesterday_closing_price))
diff_percentage = (difference / float(yesterday_closing_price))  * 100

if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

if diff_percentage > 5 :
    news_parameter = {
        
        "apikey" : NEWS_API_KEY,
        "q" : COMPANY_NAME,
    }
    news_response = requests.get(url="https://newsapi.org/v2/everything", params= news_parameter) 
    article = news_response.json()['articles']
    print(news_response.json())
    three_article = article[:3]
    print(three_article)
    formatted_articles = [f"{COMPANY_NAME} : {up_down} {diff_percentage}%\n\nHeadlines : {article['title']}. \n\nBrief : {article['description']}" for article in three_article]


    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_= "+1********",
            to= "+91*********"
        )
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

