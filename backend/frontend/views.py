from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, resolve_url
from django.contrib.auth import logout
from django.views import View
from django.conf import settings
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from .forms import LoginUserForm, RegisterUserForm
from .models import ApiKeys


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
        try:
            user_api = User.objects.get(username=request.user.username).apikeys
            self.context['api_ukraine'] = user_api.api_ukraine
            self.context['api_bodis'] = user_api.api_bodis
        except ObjectDoesNotExist:
            self.context['api_ukraine'] = ''
            self.context['api_bodis'] = ''
        return render(request, 'frontend/profile.html', context=self.context)

    def post(self, request):
        form = ApiKeys(
            username=User.objects.get(id=request.user.id),
            api_ukraine=request.POST.get('api_ukraine'),
            api_bodis=request.POST.get('api_bodis'),
        )
        form.save()
        return redirect('profile')
