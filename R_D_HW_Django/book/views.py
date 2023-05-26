from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .forms import BookForm
from .models import Book


class BooksList(ListView):
    model = Book


class DetailBook(DetailView):
    model = Book


def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect(reverse('detail-book', kwargs={'pk': book.pk}))
    else:
        form = BookForm()
    return render(request, 'book/create_book.html', {'form': form})