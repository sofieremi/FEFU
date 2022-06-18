from django.urls import path
from core.views import main, register, profile

urlpatterns = [
    path('', main, name='main'),
    path('/register', register, name='register'),
    path('/profile', profile, name='profile'),
]