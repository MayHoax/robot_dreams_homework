from django.urls import path
from .views import UsersList, UserDetail, create_user


urlpatterns = [
    path('all', UsersList.as_view(), name='user'),
    path('<int:pk>', UserDetail.as_view(), name='user-detail'),
    path('create/', create_user, name='create-user'),
]

