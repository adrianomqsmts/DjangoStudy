from django.views.generic import TemplateView, View, UpdateView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, reverse
# Mixin que extends a funcionalidade, permite ver se se o usuário está autenticado
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import TemplateView, CreateView
from django.core.exceptions import ObjectDoesNotExist
from .models import Profile, Post
from .forms import ProfileCreationForm, ProfileUpdateForm, PostCreationForm

class ProfileExistsRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        try:
            user = User.objects.get(pk=self.request.user.pk)
            try:
                profile = user.profile
            except ObjectDoesNotExist:
                return redirect('create_profile')
            return super().dispatch(request, *args, **kwargs)
        except ObjectDoesNotExist:
            return redirect('/')


class MainView(ProfileExistsRequiredMixin, LoginRequiredMixin, CreateView):
    model = Post
    template_name = "main.html"
    form_class = PostCreationForm
    #fields = '__all__'
    success_url = reverse_lazy('main')

    def get_form_kwargs(self):
        form = super().get_form_kwargs()
        form['user'] = self.request.user
        return form

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context["posts"] = Post.objects.filter(author=self.request.user)
        return context

    def form_valid(self, form, *args, **kwargs):
        form.fields['author'] = self.request.user.pk
        return super(MainView, self).form_valid(form, *args, **kwargs)

def likeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if(post.likes.filter(id=request.user.id).exists()):
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('main'))

class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    template_name = "create-profile.html"
    #fields = '__all__'
    success_url = reverse_lazy('main')

    def get_form_kwargs(self):
        form = super().get_form_kwargs()
        form['user'] = self.request.user
        return form

    def form_valid(self, form, *args, **kwargs):
        form.fields['user'] = self.request.user.pk
        return super(ProfileCreateView, self).form_valid(form, *args, **kwargs)


class ProfileUpdateView(UpdateView):
    #model = Profile
    form_class = ProfileUpdateForm
    template_name = "edit-profile.html"
    #fields = '__all__'
    success_url = reverse_lazy('main')

    def get_object(self):
        return self.request.user.profile


# class PostCreateView(CreateView.):
#     model = Post
#     success_url = reverse_lazy('main')
#     fields = '__all__'
#     template_name = "post_form.html"
