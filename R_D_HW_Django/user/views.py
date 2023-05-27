from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import User
from .forms import UserForm


class UsersList(ListView):
    model = User


class UserDetail(DetailView):
    model = User


from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UserForm
from .models import User


class CreateUser(CreateView):
    model = User
    form_class = UserForm
    template_name = 'user/create_user.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        return response

    def get_success_url(self):
        return reverse_lazy('user-detail', kwargs={'pk': self.object.pk})


