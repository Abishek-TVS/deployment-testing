from django.urls import path
from . import views

app_name = 'trapp'

urlpatterns = [
    path('register', views.register, name='registration'),
    path('user_login', views.user_login, name='user_login'),
]