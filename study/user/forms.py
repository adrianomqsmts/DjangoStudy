from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms


class CustomUserCreationForm(UserCreationForm):
  # Especificando a classe Bootstrap
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Primeiro Nome', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Sobrenome', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        # Especificando quais campos serão renderizados no formulário
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        # Inserindo a classe bootstrap para os campos padrão do formulário que já estavam criados
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
