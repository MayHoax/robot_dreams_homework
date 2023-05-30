import json
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView

from .forms import PurchaseForm
from .models import Purchase


class PurchaseList(ListView):
    model = Purchase


class PurchaseDetail(DetailView):
    model = Purchase


class CreatePurchase(CreateView):
    model = Purchase
    form_class = PurchaseForm
    template_name = 'purchase/create_purchase.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        purchase = form.save()
        return response

    def get_success_url(self):
        return reverse_lazy('purchase-detail', kwargs={'pk': self.object.pk})

