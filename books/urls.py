from django.urls import path, include
from rest_framework.routers import DefaultRouter
from books import views
from books.views import BookViewSet


router = DefaultRouter()
router.register('books', views.BookViewSet)



urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('api/', include(router.urls)),

    path('books/', views.books_view_c, name='books'),
    path('ordered_names/', views.show_ordered_names, name = 'ordered_names'),
    path('ordered_numbers/', views.ordered_numbers, name = 'ordered_numbers'),

]