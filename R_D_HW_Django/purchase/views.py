import json
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Purchase


class PurchaseList(ListView):
    model = Purchase


class PurchaseDetail(DetailView):
    model = Purchase
