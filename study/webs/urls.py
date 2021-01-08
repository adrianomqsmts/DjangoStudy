from django.urls import path, include
from .views import MainView, ProfileCreateView, ProfileUpdateView

urlpatterns = [
	path('main/', MainView.as_view(), name='main'),
	path('accounts/profile/create/', ProfileCreateView.as_view(), name='create_profile'),
	path('accounts/profile/edit/', ProfileUpdateView.as_view(), name='edit_profile'),
]