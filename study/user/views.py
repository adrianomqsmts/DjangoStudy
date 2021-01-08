from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.


class HomeView(TemplateView):
    template_name = "index.html"


class RegisterCreateView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = "registration/register.html"
    #fields = ('__all__')
    success_url = reverse_lazy('login')


class UserUpdateView(UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = "update-user.html"
    #fields = ('username', 'first_name', 'last_name', 'email')
    success_url = reverse_lazy('main')

    def get_object(self):
        return self.request.user

