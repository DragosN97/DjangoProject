from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

fruits = ['Apple', 'Pineapple', 'Durian', 'Passion fruit', 'Banana', 'Pear']

def hello(request):
    return HttpResponse("Hello from our Books app!")

def home(request):

    context = {
        'username': 'Alice',
        'logged_in': True,
        'current_time': datetime.now(),
        'fruits': fruits
    }

    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')