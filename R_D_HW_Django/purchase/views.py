# from django.urls import reverse_lazy
# from django.views.generic import ListView, DetailView, CreateView
# from .forms import PurchaseForm
# from .models import Purchase
from .serializers import PurchaseSerializer
from .models import Purchase
from rest_framework.viewsets import ModelViewSet


# class PurchaseList(ListView):
#     model = Purchase
#
# class PurchaseDetail(DetailView):
#     model = Purchase
#
# class CreatePurchase(CreateView):
#     model = Purchase
#     form_class = PurchaseForm
#     template_name = 'purchase/create_purchase.html'
#
#     def form_valid(self, form):
#         response = super().form_valid(form)
#         purchase = form.save()
#         return response
#
#     def get_success_url(self):
#         return reverse_lazy('purchase-detail', kwargs={'pk': self.object.pk})

class PurchaseViewSet(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    search_fields = ["user_id", "book_id", "date", ]
    ordering_fields = ["user_id", "book_id", "date", ]
