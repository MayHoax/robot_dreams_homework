from django.urls import path
from .views import UsersList, UserDetail, CreateUser


urlpatterns = [
    path('all', UsersList.as_view(), name='user'),
    path('<int:pk>', UserDetail.as_view(), name='user-detail'),
    path('create/', CreateUser.as_view(), name='create-user')
    ]

