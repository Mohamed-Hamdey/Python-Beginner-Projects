import requests
from twilio.rest import Client

account_sid = "AC7cd36b8b77cdf6c47852720d406f37b5"
auth_token = "26876ea2be1e1a70588f7a7850144d73"



API_KEY = "45cfef27990f159a5e2a78f3a24cc29b"
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast?lat=30.013651&lon=31.208139&cnt=3&appid=45cfef27990f159a5e2a78f3a24cc29b")
print(f"status code : {response.status_code}")
weather_data  = response.json()
data = []
rain = False
for i in range(0,3):
    data.append(weather_data["list"][i]["weather"][0]["id"])
    if data[i] < 700:
     rain = True
     
client = Client(account_sid, auth_token)

if rain:
    message = client.messages.create(
        from_='+12532592481',
        body="Bring an umbrella ☔️",
    to='+201026692641'
    )
else:
    message = client.messages.create(
  from_='+12532592481',
  body="No need for an umbrella today 🌞",
  to='+201026692641'
)
print("sent successfully")   