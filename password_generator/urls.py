from django.urls import path
from generator import views

urlpatterns = [
    path('', views.index),
    path('password-result/', views.result, name='result'),
]
