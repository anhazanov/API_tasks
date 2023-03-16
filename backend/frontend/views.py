from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, resolve_url
from django.contrib.auth import logout
from django.views import View
from django.conf import settings
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import LoginUserForm, RegisterUserForm, AddApiKeys


class RegisterPage(CreateView):
    form_class = RegisterUserForm
    template_name = 'frontend/register.html'
    success_url = reverse_lazy('profile')


class LoginPage(LoginView):
    """
    Login user on start page (url 'login')
    """
    form_class = LoginUserForm
    template_name = 'frontend/login.html'

    def get_success_url(self):
        return resolve_url(settings.LOGIN_REDIRECT_URL)


def logout_user(request):
    """
    Logout user and redirect on start page
    """
    logout(request)
    return redirect('index')


class ProfilePage(View):
    context = {}

    def get(self, request):
        self.context['form'] = AddApiKeys()
        return render(request, 'frontend/profile.html', context=self.context)

    def post(self, request):
        form = AddApiKeys(request.POST)
        print(request.POST)
        print(form)
        # if form.is_valid():
        #     form.save()
        return redirect('profile')
