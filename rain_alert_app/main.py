import requests

api_key = "1b3df87e59188802f6486f803ebfffa0"
weather_params = {
"lat": 47.376888,
"lon": 8.541694,
"exclude": "current,minutely,daily",
"units": "metric",
"appid": api_key
}
OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
response = requests.get(OWM_endpoint, params=weather_params)
# print(response.status_code)
response.raise_for_status()
weather_data = response.json()

will_rain = False
weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    if condition_code < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella.")
