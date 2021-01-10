from django.views.generic import TemplateView, View, UpdateView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, reverse
# Mixin que extends a funcionalidade, permite ver se se o usuário está autenticado
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import TemplateView, CreateView, ListView
from django.core.exceptions import ObjectDoesNotExist
from .models import Profile, Post, Comment
from .forms import ProfileCreationForm, ProfileUpdateForm, PostCreationForm, CommentCreationForm, CommentUpdateForm
import json
from django.core import serializers
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


def commentUpdateView(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CommentUpdateForm(request.POST, instance=comment)
        # check whether it's valid:
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def commentDeleteView(request, pk):
    comment = get_object_or_404(Comment, id=pk)
    comment.delete()
    messages.success(request, 'O comentário foi removido com sucesso')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


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
    # fields = '__all__'
    success_url = reverse_lazy('main')

    def get_form_kwargs(self):
        form = super().get_form_kwargs()
        form['user'] = self.request.user
        return form

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        friends = self.request.user.profile.friends.all()
        posts = Post.objects.filter(author__in=friends) | Post.objects.filter(
            author=self.request.user)
        context['posts'] = posts.order_by('-post_date')
        return context

    def form_valid(self, form, *args, **kwargs):
        form.fields['author'] = self.request.user.pk
        return super(MainView, self).form_valid(form, *args, **kwargs)


def commentView(request):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    comments = post.comments.all()
    jsonComments = serializers.serialize("json", comments)
    #jsonPost = serializers.serialize("json", post)
    context = {
        "comments": jsonComments,
        "title": post.title,
        "body": post.body,
    }
    return HttpResponse(json.dumps(context), content_type='application/json')


class CommentCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = "list-comment.html"
    #fields = '__all__'
    #success_url = reverse_lazy('')

    success_message = "Comment was created successfully"

    def get_success_url(self):
        return self.request.path

    def get_form_kwargs(self):
        form = super().get_form_kwargs()
        form['user'] = self.request.user
        form['post'] = Post.objects.get(pk=self.kwargs['pk'])
        return form

    def get_context_data(self, **kwargs):
        context = super(CommentCreateView, self).get_context_data(**kwargs)
        context['post'] = Post.objects.get(pk=self.kwargs['pk'])
        context['comments'] = Comment.objects.filter(post=self.kwargs['pk'])
        return context

    def form_valid(self, form, *args, **kwargs):
        form.fields['author'] = self.request.user.pk
        return super(CommentCreateView, self).form_valid(form, *args, **kwargs)


def likeView(request):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if(post.likes.filter(id=request.user.id).exists()):
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    # Resposta para o ajax
    context = {
        "liked": liked,
        "total_likes": post.total_likes(), }
    return HttpResponse(json.dumps(context), content_type='application/json')


class ProfileCreateView(LoginRequiredMixin, CreateView):
    model = Profile
    form_class = ProfileCreationForm
    template_name = "create-profile.html"
    # fields = '__all__'
    success_url = reverse_lazy('main')

    def get_form_kwargs(self):
        form = super().get_form_kwargs()
        form['user'] = self.request.user
        return form

    def form_valid(self, form, *args, **kwargs):
        form.fields['user'] = self.request.user.pk
        return super(ProfileCreateView, self).form_valid(form, *args, **kwargs)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    # model = Profile
    form_class = ProfileUpdateForm
    template_name = "edit-profile.html"
    # fields = '__all__'
    success_url = reverse_lazy('main')

    def get_object(self):
        return self.request.user.profile


# class PostCreateView(CreateView.):
#     model = Post
#     success_url = reverse_lazy('main')
#     fields = '__all__'
#     template_name = "post_form.html"
