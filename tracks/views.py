from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Track, Resources, Bookmark
from .forms import *
# Create your views here.

class TrackListView(LoginRequiredMixin, ListView):
    model = Track
    template_name = 'track.html'
    context_object_name = 'tracks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_bookmarks = Bookmark.objects.filter(user=self.request.user).values_list('track_id', flat=True)
        context['user_bookmarks'] = user_bookmarks
        return context

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
    
class TrackCreateView(LoginRequiredMixin, CreateView):
    model = Track
    form_class = TrackCreateForm
    template_name = 'track_create.html'
    success_url = reverse_lazy('track_list')


class TrackUpdateView(LoginRequiredMixin, UpdateView):
    model = Track
    form_class = TrackUpdateForm
    template_name = 'track_update.html'
    context_object_name = 'track'
    success_url = reverse_lazy('track_list')

class TrackDeleteView(LoginRequiredMixin, DeleteView):
    model = Track
    template_name = 'track_confirm_delete.html'
    success_url = reverse_lazy('track_list')

class ResourceCreateView(LoginRequiredMixin, CreateView):
    model = Track
    form_class = ResourceCreateForm
    template_name = 'create_resource.html'
    success_url = reverse_lazy('track_list')

class ResourcesDeleteView(LoginRequiredMixin, DeleteView):
    model = Resources
    template_name = "resources_confirm_delete.html"
    success_url = reverse_lazy('track_list')

class BookmarkToggleView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        track_slug = kwargs.get('slug')
        track = get_object_or_404(Track, slug=track_slug)
        bookmark, created = Bookmark.objects.get_or_create(user=request.user, track=track)

        if not created:
            bookmark.delete()

        return redirect(reverse_lazy('bookmarks'))
    
class BookmarkListView(LoginRequiredMixin, ListView):
    model = Bookmark
    template_name = 'bookmark_list.html'
    context_object_name = 'bookmarks'

    def get_queryset(self):
        return Bookmark.objects.filter(user=self.request.user)
    

class BookmarkRemoveView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        bookmark = get_object_or_404(Bookmark, id=kwargs['id'], user=request.user)
        bookmark.delete()
        return redirect(reverse_lazy('bookmarks'))
