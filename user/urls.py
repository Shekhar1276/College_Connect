# user/urls.py
from django.urls import path
from .views import signup, signin, signout  # Import the new view

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),  # Add this line
    # Add other URLs as needed
]
