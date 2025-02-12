import requests
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from .email_service import get_weather,send_mail
class WeatherAPIView(APIView):
    def get(self, request,lat,lon):
        API_KEY="233806f0e52a49f586e64724251002"
        url=f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={lat},{lon}"
        response = requests.get(url)
        if response.status_code != 200:
            return Response({"message":"Something went wrong"},status=response.status_code)
        if response.status_code == 400:
            return Response({"message":"Invalid city name"},status=response.status_code)
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
        return Response({"shahar":data['city']['name'],"forecast":forecast_list})
        
class WeatherEmailAPIView(APIView):
    def post(self, request):
        email=request.data.get("email")
        city=request.data.get("city")
        if not email or not city:
            return Response({"message":"Email va shahar nomini kiriting"},status=400)
        send_mail(email,city)
        return Response({"message":send_mail(email,city)})

class SubscribeAPIView(APIView):
    def post(self, request):
        email=request.data.get("email")
        city=request.data.get("city")
        if not email or not city:
            return Response({"message":"Emailni kiriting"},status=400)
        if not settings.EMAIL_HOST_USER:
            return Response({"message":"Email sozlamalari to'g'ri kiritilmagan"},status=500)
        send_mail(email,"Tashrifingiz uchun rahmat")
        Subscriber.objects.create(email=email,city=city)
        return Response({"message":"Email muvaffaqiyatli yuborildi"})