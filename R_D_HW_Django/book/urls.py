from django.urls import path
from .views import BooksList, DetailBook, CreateBook

urlpatterns = [
    path('all', BooksList.as_view(), name='books'),
    path('<int:pk>', DetailBook.as_view(), name='book-detail'),
    path('create', CreateBook.as_view(), name='create-book')

]