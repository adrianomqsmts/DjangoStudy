from django.urls import path, include
from .views import HomeView, RegisterCreateView, UserUpdateView, PasswordUpdateView, PasswordSuccessView, CustomLoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    #Rota para o sistema de autenticação pronto do Django
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', RegisterCreateView.as_view(), name='register'),
    path('accounts/password/', PasswordUpdateView.as_view(), name='password'),
    path('accounts/password_change/done', PasswordSuccessView.as_view(), name='password_success'),
    path('accounts/update/', UserUpdateView.as_view(), name='update_user'),
]

