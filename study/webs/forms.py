from django import forms
from .models import Profile, Post


class ProfileCreationForm(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        super(ProfileCreationForm, self).__init__(*args, **kwargs)
        self.fields['user'].initial = user.pk
        # self.fields['user'].selected =

    class Meta:
        model = Profile
        fields = ('user', 'bio', 'age', 'gender', 'profile_pic',
                  'facebook_url', 'twitter_url', 'instagram_url')

        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'type': 'hidden'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control', }),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control-file'}),
            'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),
            'twitter_url': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ProfileUpdateForm(forms.ModelForm):
    """Form definition for ProfileUpdate."""

    class Meta:
        """Meta definition for ProfileUpdateform."""

        model = Profile
        fields = ('bio', 'gender', 'profile_pic',
                  'facebook_url', 'twitter_url', 'instagram_url')

        widgets = {
            # 'user': forms.TextInput(attrs={'class': 'form-control', 'value': '' ,'type': 'hidden'}),
            # 'age': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control', }),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control-file'}),
            'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),
            'twitter_url': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PostCreationForm(forms.ModelForm):
    """Form definition for PostCreation."""

    def __init__(self, user, *args, **kwargs):
        super(PostCreationForm, self).__init__(*args, **kwargs)
        self.fields['author'].initial = user.pk

    class Meta:
        """Meta definition for PostCreationform."""

        model = Post
        fields = ('title', 'author', 'body', 'file')

        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'type': 'hidden'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'file': forms.FileInput(attrs={'class': 'form-control-file'}),
        }
