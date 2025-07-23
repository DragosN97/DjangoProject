from django.urls import path, include
from rest_framework.routers import DefaultRouter
from books import views

router = DefaultRouter()
router.register('books', views.BookViewSet)



urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    #path('create_book', views.create_book, name = 'create_book'),
    path('api/', include(router.urls)),

]