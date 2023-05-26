from django.urls import path
from .views import PurchaseList, PurchaseDetail

urlpatterns = [
    path('all', PurchaseList.as_view(), name='purchases'),
    path('<int:pk>', PurchaseDetail.as_view(), name='purchase-detail')
]