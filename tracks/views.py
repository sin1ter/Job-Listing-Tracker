from typing import Any
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Track, Resources
from .forms import *
# Create your views here.

class TrackListView(LoginRequiredMixin, ListView):
    model = Track
    template_name = 'track.html'
    context_object_name = 'track'

class TrackDetailView(LoginRequiredMixin, DetailView):
    model = Track
    template_name = 'track_detail.html'
    context_object_name = 'track'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        track = self.get_object()
        resources = Resources.objects.filter(title=track)
        context['resources'] = resources
        return context
    
class TrackCreateView(CreateView):
    model = Track
    form_class = TrackCreateForm
    template_name = 'track_create.html'
    success_url = reverse_lazy('track_list')


class TrackUpdateView(UpdateView):
    model = Track
    form_class = TrackUpdateForm
    template_name = 'track_update.html'
    context_object_name = 'track'
    success_url = reverse_lazy('track_list')

class TrackDeleteView(DeleteView):
    model = Track
    template_name = 'track_confirm_delete.html'
    success_url = reverse_lazy('track_list')

class ResourceCreateView(CreateView):
    model = Track
    form_class = ResourceCreateForm
    template_name = 'create_resource.html'
    success_url = reverse_lazy('track_list')

class ResourcesDeleteView(DeleteView):
    model = Resources
    template_name = "resources_confirm_delete.html"
    success_url = reverse_lazy('track_list')
