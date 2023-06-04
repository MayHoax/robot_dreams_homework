from .serializers import UserSerializer
from .models import User
from rest_framework.viewsets import ModelViewSet
from .pagination import CustomPaginator


# class UsersList(ListView):
#     model = User
#
# class UserDetail(DetailView):
#     model = User
#
#
# class CreateUser(CreateView):
#     model = User
#     form_class = UserForm
#     template_name = 'user/create_user.html'
#
#     def form_valid(self, form):
#         response = super().form_valid(form)
#         user = form.save()
#         return response
#
#     def get_success_url(self):
#         return reverse_lazy('user-detail', kwargs={'pk': self.object.pk})


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPaginator
    search_fields = ["first_name", "age"]
    ordering_fields = ["first_name", "age"]

