import requests

parameters = {"lat":25.448730,
"lon":78.570130,
"exclude":"current,minutely,daily",
"appid":"b61f185cb872f47f10bb8eb8a07d14f4"}

weather_response = requests.get("https://api.openweathermap.org/data/2.5/onecall",params = parameters)
weather_response.raise_for_status()
weather_data = weather_response.json()
codes = []
for i in range(12):
    codes.append(weather_data['hourly'][i]['weather'][0]['id'])


j = 0
flag = True
while flag and j<len(codes):
    if codes[j]<700:
        print("Bring an umbrella")
        flag = False
    else:j+=1

# hourly[0].weather[0].id

