# urls.py
from django.urls import path
from ChatApp import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('chat/', views.chat, name='chat'),
    path('token/', views.token_balance, name='token_balance'),
]