from django.urls import path
from generator import views

urlpatterns = [
    path('', views.index, name='index'),
    path('password-result/', views.result, name='result'),
    path('about/', views.about, name='about')
]
