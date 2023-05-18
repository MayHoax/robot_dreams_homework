import json

from django.http import HttpResponse

from .models import Purchase


# Create your views here.


def purchases(request):
    purchase_query = Purchase.objects.all().values()
    purchase_json = json.dumps(list(purchase_query), ensure_ascii=False, default=str)
    return HttpResponse(purchase_json)