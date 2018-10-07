import requests
import pprint

apiKey="432b69ea152f7bb18ba88191efcff460"

s=input('---> ')

p = {
   'q': s,
   'appid': apiKey,
   'units': 'imperial'
}

response=requests.get('http://api.openweathermap.org/data/2.5/weather', params=p)

weather_data = response.json()

city = weather_data['name']
print(city)

#main_data= weather_data['main']
#temperature = main_data['temp']

temperature = weather_data['main']['temp']
print(temperature)

message ='the weather in {} is {} degrees Fahrenheit.'.format(city, temperature)
print(message)


pprint.pprint(weather_data)

apiKey="be41c4e1"
params = {
   'api_key':apiKey,
   'api_secret':'3e74b84059ee73d6',
   'from':'12565420688',
   'to':'12407796433',
   'text':message,
}

requests.get('https://rest.nexmo.com/sms/json', params=params)





