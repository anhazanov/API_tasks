from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import ApiKeys


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        }


class AddApiKeys(forms.ModelForm):
    username = forms.CharField(widget=forms.HiddenInput(), required = False)
    api_ukraine = forms.CharField(label='API для Ukraine.com.ua', widget=forms.TextInput(attrs={'class': 'form-input'}))
    api_bodis = forms.CharField(label='API для Bodis.com', widget=forms.TextInput(attrs={'class': 'form-input'}))
    class Meta:
        model = ApiKeys
        fields = ['username', 'api_ukraine', 'api_bodis']
