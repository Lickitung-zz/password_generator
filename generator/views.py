import random, string

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'generator/index.html')

def result(request):
    password = ""
    characters = list('abcdefghijklmopqrstuvwxyz')
    length = int(request.GET.get('length',12))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+?.,'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    for i in range(length):
        password += random.choice(characters)

    return render(request, 'generator/result.html', {'password':password})

def about(request):
    return render(request, 'generator/about.html')