from django.urls import path, include
from .views import MainView, ProfileCreateView, ProfileUpdateView, likeView, CommentCreateView, commentDeleteView, commentUpdateView

urlpatterns = [
	path('main/', MainView.as_view(), name='main'),
	path('accounts/profile/create/', ProfileCreateView.as_view(), name='create_profile'),
	path('accounts/profile/edit/', ProfileUpdateView.as_view(), name='edit_profile'),
	path('like/', likeView, name='like_post'),
	path('post/<int:pk>', CommentCreateView.as_view(), name='comments_post'),
	path('comment/remove/<int:pk>', commentDeleteView, name='remove_comment'),
	path('comment/update/<int:pk>', commentUpdateView, name='update_comment'),
]