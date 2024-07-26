from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView

from .forms import CustomUserCreationForm, EditProfileForm
from .models import *
from .mixins import AnonymousRequiredMixin

class SignUpView(AnonymousRequiredMixin, CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class CustomLoginView(AnonymousRequiredMixin, LoginView):
    template_name = 'registration/login.html'

class ProfileView(LoginRequiredMixin, DetailView):
    model = CustomUserModel
    template_name = 'registration/profile.html'

    def get_object(self):
        return self.request.user


class EditProfileView(LoginRequiredMixin, UpdateView):
    model = CustomUserModel
    form_class = EditProfileForm
    template_name = "registration/edit_profile.html"
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user
        