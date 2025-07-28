import json
from operator import invert

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from datetime import datetime

from django.template.context_processors import request

from books.forms import BookForm
from books.models import Book
from rest_framework import viewsets
from books.serializers import BookSerializers
from django.views.decorators.csrf import csrf_exempt
from books.forms import BookForm


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


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

book_list = ["Book1", "Mockingbirds", "Ex1"]

@csrf_exempt
def book_view(request: HttpRequest):
    if request.method == "GET":
        book_list.sort()
        context = {
            "books": book_list
        }
        return render(request, 'books.html', context)
    elif request.method == "POST":
        data = json.loads(request.body)
        book_title = data["title"]
        book_list.append(book_title)
        return HttpResponse("")

@csrf_exempt
def books_view_c(request: HttpRequest):
    if request.method == "GET":
        context = {
            'form': BookForm()

        }
        return render(request, 'create_book.html', context)
    elif request.method == "POST":
        form_with_data = BookForm(request.POST)
        if form_with_data.is_valid():
            form_with_data.save()
            return HttpResponse("Book save successfully!")
        else:
            return HttpResponse(form_with_data.errors)


names = [
    "Andrei", "Maria", "Ion", "Elena", "Alexandru", "Ana",
    "Vasile", "Ioana", "George", "Gabriela", "Florin", "Mihai",
    "Diana", "Radu", "Laura", "Cristian", "Raluca",
    "Bianca",
]

def show_ordered_names(request: HttpRequest):
    if request.method == "GET":
        names.sort()
        context = {
            'ordered_names': names
        }
        return render(request, 'ordered_names.html', context)



numbers = [73, 28, 95, 14, 61, 39, 87, 5, 46, 32]

def ordered_numbers(request: HttpRequest):
    if request.method == "GET":
        numbers.sort(reverse = True)
        context = {
            'ordered_numbers': numbers
        }
        return render(request, 'ordered_numbers.html', context)