from django.views.generic import TemplateView, View, UpdateView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
# Mixin que extends a funcionalidade, permite ver se se o usuário está autenticado
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import TemplateView, CreateView
from django.core.exceptions import ObjectDoesNotExist
from .models import Profile
from .forms import ProfileCreationForm, ProfileUpdateForm
#from .models import Post


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


class MainView(ProfileExistsRequiredMixin, LoginRequiredMixin, TemplateView):
    template_name = "main.html"

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        #context["user"] = User.objects.filter(author=self.request.user)
        return context



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
