from django.urls import path
from .views import TrackListView, TrackDetailView, TrackCreateView, TrackUpdateView, TrackDeleteView, ResourceCreateView, ResourseDeleteView


urlpatterns = [
    path('', TrackListView.as_view(), name='track_list'),
    path('track-create/', TrackCreateView.as_view(), name='create_track'),
    path('track-update/<slug:slug>', TrackUpdateView.as_view(), name='update_track'),
    path('track-delete/<slug:slug>', TrackDeleteView.as_view(), name='delete_track'),
    path('detail/<slug:slug>/', TrackDetailView.as_view(), name='keeptrackdetail'),

    path('resource-create/<slug:slug>/', ResourceCreateView.as_view(), name='create_resources'),
    path('resource-delete/<slug:slug>/delete/', ResourseDeleteView.as_view(), name='delete_resource'),
] 

