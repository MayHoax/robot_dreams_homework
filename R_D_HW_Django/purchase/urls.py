from django.urls import path
from .views import PurchaseList, PurchaseDetail, CreatePurchase


urlpatterns = [
    path('all', PurchaseList.as_view(), name='purchases'),
    path('<int:pk>', PurchaseDetail.as_view(), name='purchase-detail'),
    path('create', CreatePurchase.as_view(), name='create-purchase')
]