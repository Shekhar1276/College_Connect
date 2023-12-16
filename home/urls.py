# home/urls.py
from django.urls import path
from .views import home
from .views import team

urlpatterns = [
    path('', home, name='home'),
    path('about/team', team, name='team')
]
