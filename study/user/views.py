from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm

# Create your views here.


class HomeView(TemplateView):
    template_name = "index.html"


class RegisterCreateView(CreateView):
    #model = User
    form_class = CustomUserCreationForm
    template_name = "registration/register.html"
    #fields = ('__all__')
    success_url = reverse_lazy('login')
