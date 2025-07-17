from django.urls import path
from books import views

urlpatterns = [
    path('hello', views.hello, name='hello'),
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
]