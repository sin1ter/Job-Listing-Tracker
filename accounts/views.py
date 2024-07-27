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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        resume_url = user.resume.url if user.resume else None
        context['resume_url'] = resume_url
        context['is_pdf'] = resume_url.endswith('.pdf') if resume_url else False
        context['is_pdf'] = resume_url.endswith('.doc') or resume_url.endswith('.docx') if resume_url else False
        return context


class EditProfileView(LoginRequiredMixin, UpdateView):
    model = CustomUserModel
    form_class = EditProfileForm
    template_name = "registration/edit_profile.html"
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user
        