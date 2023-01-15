import requests
import os
from twilio.rest import Client

api_key = ""
LAT = 51.5579
LNG = 12.9916
EXCLUDE = ""


ep = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "lat": LAT,
    "lon": LNG,
    "appid": api_key,
    "units": "metric"
}

def notify_about_weather():
    # Set environment variables for your credentials
    # Read more at http://twil.io/secure
    account_sid = ""
    auth_token = ""
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's cold outside, wear a sweater!",
        from_="",
        to=""
    )
    print(message.status)

def is_it_cold():
    response = requests.get(url=ep, params=params)
    response.raise_for_status()
    temp = response.json()["main"]["temp"]
    if temp < 15:
        return True
    return False


if is_it_cold():
    notify_about_weather()