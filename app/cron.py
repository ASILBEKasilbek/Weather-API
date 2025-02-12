import requests
from django_cron import CronJobBase, Schedule
from django.core.mail import send_mail
from .models import Subscriber

# API ma'lumotlari
API_KEY = "233806f0e52a49f586e64724251002"
EMAIL_FROM = "asilbek.sadullayev000@gmail.com"

# Ob-havo ma’lumotlarini olish uchun funksiya
def get_weather(city):
    url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}&days=5"
    response = requests.get(url)

    if response.status_code != 200:
        return {"message": "Something went wrong"}

    data = response.json()

    forecast_list = []
    for item in data['forecast']['forecastday']:  # To‘g‘ri JSON kalitlari ishlatilmoqda
        forecast_list.append({
            "date": item['date'],
            "temp": item['day']['avgtemp_c'],  # O‘rtacha harorat
            "feels_like": item['day']['avgtemp_c'],
            "temp_min": item['day']['mintemp_c'],
            "temp_max": item['day']['maxtemp_c'],
            "pressure": item['day'].get('pressure_mb', 'N/A'),  # Ba'zan mavjud bo‘lmasligi mumkin
            "humidity": item['day']['avghumidity'],
            "weather": item['day']['condition']['text'],
            "icon": item['day']['condition']['icon'],
        })

    return {"shahar": data['location']['name'], "forecast": forecast_list}

# Django CronJob sinfi
class SendWeatherEmailsCronJob(CronJobBase):
    RUN_EVERY_MINS = 60  # Har soatda ishga tushadi
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'weather_app.send_weather_emails'  # Ilova nomiga mos yozish kerak

    def do(self):
        subscribers = Subscriber.objects.all()
        for subscriber in subscribers:
            data = get_weather(subscriber.city)
            if data.get("message"):
                continue  # Xatolik bo‘lsa, davom etamiz

            forecast = data['forecast']
            forecast_text = ""
            for item in forecast:
                forecast_text += f"{item['date']}:\n"
                forecast_text += f"Temp: {item['temp']}°C\n"
                forecast_text += f"Feels like: {item['feels_like']}°C\n"
                forecast_text += f"Min Temp: {item['temp_min']}°C\n"
                forecast_text += f"Max Temp: {item['temp_max']}°C\n"
                forecast_text += f"Pressure: {item['pressure']} hPa\n"
                forecast_text += f"Humidity: {item['humidity']}%\n"
                forecast_text += f"Weather: {item['weather']}\n\n"

            send_mail(
                'Weather Forecast',
                f"{data['shahar']} uchun ob-havo ma'lumotlari:\n\n{forecast_text}",
                EMAIL_FROM,
                [subscriber.email],
                fail_silently=False,
            )
