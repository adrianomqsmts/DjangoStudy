from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms


class CustomUserCreationForm(UserCreationForm):
  # Especificando a classe Bootstrap
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Primeiro Nome', max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Sobrenome', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control'}))

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


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        # Especificando quais campos serão renderizados no formulário
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email')

    def __init__(self, *args, **kwargs):
        # Inserindo a classe bootstrap para os campos padrão do formulário que já estavam criados
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'type': 'password'}
        ),
        label='Senha antiga:'
    )
    new_password1 = forms.CharField(
        label='Nova Senha:',
        max_length=100,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'type': 'password'}
        ),
        help_text='Sua senha não pode ser muito parecida com o resto das suas informações pessoais.<br/> Sua senha precisa conter pelo menos 8 caracteres.<br/> Sua senha não pode ser uma senha comumente utilizada.<br/> Sua senha não pode ser inteiramente numérica.<br/>'
    )
    new_password2 = forms.CharField(
        label='Repetir nova senha:',
        max_length=100,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'type': 'password'}
        )
    )

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

