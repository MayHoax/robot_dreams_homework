from django.http import HttpResponse
from .models import User
import json


def user(request):
    user_query = User.objects.all().values()
    user_json = json.dumps(list(user_query))
    return HttpResponse(user_json)
