from django.core.mail import send_mail
from django.http import JsonResponse
import requests

API_KEY="233806f0e52a49f586e64724251002"
EMAIL_FROM="asilbek.sadullayev000@gamil.com"

def get_weather(city):
    url=f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
    response = requests.get(url)
    if response.status_code != 200:
        return {"message":"Something went wrong"}
    if response.status_code == 400:
        return {"message":"Invalid city name"}
    data = response.json()
    forecast_list=[]
    for item in data['list'][:5]:
        forecast_list.append({
            "date":item['dt_txt'],
            "temp":item['main']['temp'],
            "feels_like":item['main']['feels_like'],
            "temp_min":item['main']['temp_min'],
            "temp_max":item['main']['temp_max'],
            "pressure":item['main']['pressure'],
            "humidity":item['main']['humidity'],
            "weather":item['weather'][0]['description'],
            "icon":item['weather'][0]['icon'],
        })
    return {"shahar":data['city']['name'],"forecast":forecast_list}

def send_email(email,city):
    data=get_weather(city)
    if data.get("message"):
        return JsonResponse(data)
    forecast=data['forecast']
    forecast_text=""
    for item in forecast:
        forecast_text+=f"{item['date']}:\n\n"
        forecast_text+=f"Temp:{item['temp']}\n"
        forecast_text+=f"Feels like:{item['feels_like']}\n"
        forecast_text+=f"Temp min:{item['temp_min']}\n"
        forecast_text+=f"Temp max:{item['temp_max']}\n"
        forecast_text+=f"Pressure:{item['pressure']}\n"
        forecast_text+=f"Humidity:{item['humidity']}\n"
        forecast_text+=f"Weather:{item['weather']}\n"
        forecast_text+=f"Icon:{item['icon']}\n\n"
    send_mail(
        'Weather forecast',
        f"{data['shahar']} haqida ma'lumot:\n\n{forecast_text}",
        EMAIL_FROM,
        [email],
        fail_silently=False,
    )
    return JsonResponse({"message":"Email sent"})
    