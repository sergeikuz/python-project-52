from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.views.generic import ListView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth import logout


class UserListView(ListView):
    model = User
    template_name = 'users/user_list.html'
    context_object_name = 'users'

class UserCreateView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('login')

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('user_list')  # Направляет на страницу профиля после обновления

    def get_object(self, queryset=None):
        # Возвращает только текущего пользователя
        return self.request.user

class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'users/user_confirm_delete.html'
    success_url = reverse_lazy('index')  # Или на любую другую страницу после удаления

    def get_object(self, queryset=None):
        # Позволяет удалять только свои данные
        return self.request.user
    
    def delete(self, request, *args, **kwargs):
        # При удалении пользователя, выходим из системы
        obj = self.get_object()
        logout(self.request)
        return super().delete(request, *args, **kwargs)


# Create your views here.
