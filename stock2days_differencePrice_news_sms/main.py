import requests
from twilio.rest import Client



STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

stock_url = "https://www.alphavantage.co/query"
stock_api_key = "***************************"

news_url ="https://newsapi.org/v2/everything"
news_api_key = "***************************"

account_sid = "AC60ca67a2c3938b3ab670501585eff434"
auth_token = "***************************"

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


stock_para = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": stock_api_key
}

data = requests.get(stock_url, params=stock_para)
stock_data = data.json()["Time Series (Daily)"]
stock_data_list = [value for (key,value) in stock_data.items()]
yesterday = stock_data_list[0]["4. close"]
day_before_yesterday = stock_data_list[1]["4. close"]

difference = abs(float(day_before_yesterday) - float(yesterday))
percent_of_inc = (difference / float(yesterday)) * 100

if percent_of_inc > 5:
    news_para = {
        "apiKey": news_api_key,
        "qInTitle": COMPANY_NAME,
    }

    data = requests.get(news_url,params=news_para)
    news_data = data.json()["articles"]
    three_article = news_data[:3]
    print(three_article)

    three_news = [f"Headline: {article['title']}.\nBrief: {article['description']}" for article in three_article]
    client = Client(account_sid, auth_token)
    for article in three_news:
        message = client.messages.create(
            body=article,
            from_="twilio_gen_num",
            to="your_num"
        )
        print(message.sid)

