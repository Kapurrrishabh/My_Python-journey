import requests
import json
import os
city=input("Enter the city you want Weather of:-")
url=f"http://api.weatherapi.com/v1/forecast.json?key=5261101ca9bc41a985175620252601&q={city}&days=1&aqi=no&alerts=no"
response=requests.get(url)

response_dic=json.loads(response.text)
# print(response_dic)
# print(f"weather of {city} is:")
# print(f"temperature is:{response_dic["current"]["temp_c"]}")
os.system(f"say 'temperature of {city} is:{response_dic["current"]["temp_c"]} degrees celcius'")
os.system(f"say ' weather condition is:{response_dic["current"]["condition"]["text"]} '")