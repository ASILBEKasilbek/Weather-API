from django.urls import path
from .views import WeatherAPIView

urlpatterns = [
    path('weather/<str:lat>/<str:lon>/',WeatherAPIView.as_view()),
    path('email/',WeatherEmailAPIView.as_view()),
    path('subscribe/',SubscribeAPIView.as_view()),
]