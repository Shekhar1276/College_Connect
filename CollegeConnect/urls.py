# CollegeConnect/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('user.urls')), 

    # Add more URL patterns for other apps if needed
]
