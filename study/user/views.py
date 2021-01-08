from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView, LoginView
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomPasswordChangeForm
from django.contrib.auth import logout

# Create your views here.

class NotLoginRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return super().dispatch(request, *args, **kwargs)


class CustomLoginView(NotLoginRequiredMixin, LoginView):
    template_name = 'registration/login.html'

class HomeView(TemplateView):
    template_name = "index.html"


class RegisterCreateView(NotLoginRequiredMixin, CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = "registration/register.html"
    #fields = ('__all__')
    success_url = reverse_lazy('login')


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = "update-user.html"
    #fields = ('username', 'first_name', 'last_name', 'email')
    success_url = reverse_lazy('main')

    def get_object(self):
        return self.request.user


class PasswordUpdateView(LoginRequiredMixin, PasswordChangeView):
    #model = User
    form_class = CustomPasswordChangeForm
    template_name = "update-password.html"
    success_url = reverse_lazy('password_success')

    # def get_object(self):
    #     return self.request.user

    def form_valid(self, form, *args, **kwargs):
        form.save()
        logout(self.request)
        return super(PasswordUpdateView, self).form_valid(form)


class PasswordSuccessView(TemplateView):
    template_name = "password-success.html"
