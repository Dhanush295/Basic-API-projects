import requests
from twilio.rest import Client


ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
api = "weather api "
auth_token = "twilio auth token key  "
account_sid = "twilio sid key"
weather_para = {
    "appid": api,
    "lat": 33.770050,
    "lon": -118.193741,
    "exclude": 'coord,base,main,visibility,wind,clouds,dt,sys,timezone,id,name',
}


data = requests.get(ENDPOINT, params=weather_para)
weather_data = data.json()
condition_code = weather_data['weather'][0]['id']

if condition_code < 700:
    
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Its raining outside dont forget to take your ☂",
        from_="generated num",
        to="your number"
    )
    print(message.status)

