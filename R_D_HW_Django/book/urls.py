from django.urls import path
from .views import BooksList, DetailBook, create_book

urlpatterns = [
    path('all', BooksList.as_view(), name='books'),
    path('<int:pk>', DetailBook.as_view(), name='detail-book'),
    path('create', create_book, name='create-book')

]