from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('ru/', views.welcome_ru, name='welcome-ru'),
    path('main/', views.main, name='main'),
    path('main-ru/', views.main_ru, name='main-ru'),
]