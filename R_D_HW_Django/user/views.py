from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import User
from .forms import UserForm


class UsersList(ListView):
    model = User


class UserDetail(DetailView):
    model = User


def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()  # Сохраняем форму и получаем объект пользователя
            return redirect(reverse('user-detail', kwargs={'pk': user.pk}))  # Перенаправляем на страницу с ID пользователя
    else:
        form = UserForm()
    return render(request, 'user/create_user.html', {'form': form})