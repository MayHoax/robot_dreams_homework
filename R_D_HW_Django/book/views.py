# from django.urls import reverse_lazy
# from django.views.generic import ListView, DetailView, CreateView
# from .forms import BookForm
# from .models import Book
from .serializers import BookSerializer
from .models import Book
from rest_framework.viewsets import ModelViewSet
#
# class BooksList(ListView):
#     model = Book
#
# class DetailBook(DetailView):
#     model = Book
#
# class CreateBook(CreateView):
#     model = Book
#     form_class = BookForm
#     template_name = 'book/create_book.html'
#
#     def form_valid(self, form):
#         response = super().form_valid(form)
#         book = form.save()
#         return response
#
#     def get_success_url(self):
#         return reverse_lazy('book-detail', kwargs={'pk': self.object.pk})


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    search_fields = ["title", "author", "year", "price"]
    ordering_fields = ["title", "author", "year", "price"]

