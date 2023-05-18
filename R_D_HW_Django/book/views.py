from django.http import HttpResponse
from .models import Book
import json
# Create your views here.


def books(request):
    book_query = Book.objects.all().values()
    book_json = json.dumps(list(book_query), ensure_ascii=False, default=str)
    return HttpResponse(book_json)