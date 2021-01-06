from django.urls import path, include
from .views import HomeView, RegisterCreateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    #Rota para o sistema de autenticação pronto do Django
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', RegisterCreateView.as_view(), name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html') , name='login'),
]

