from django.http import HttpResponse
from .models import Purchase
import json
# Create your views here.


def purchases(request):
    book_query = Purchase.objects.all().values()
    book_json = json.dumps(list(book_query), ensure_ascii=False, default=str)
    return HttpResponse(book_json)