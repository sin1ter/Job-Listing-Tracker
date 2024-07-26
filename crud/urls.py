from django.urls import path
from .views import dashboard, JobListView, JobDetailView, JobCreateView, JobUpdateView, JobDeleteView, RecruiterCreateView, RecruiterListView, RecruiterDetailView, RecruiterDeleteView, RecruiterUpdateView

urlpatterns = [

    path('dashboard/', dashboard, name='dashboard'),

    path('', JobListView.as_view(), name='job_list'),
    path('create/', JobCreateView.as_view(), name='job_create'),
    path('detail/<slug:slug>/',JobDetailView.as_view(), name='job_detail'),
    path('update/<slug:slug>/',JobUpdateView.as_view(), name='job_update'),
    path('<slug:slug>/delete/',JobDeleteView.as_view(), name='job_delete'),

    path('recruiter/', RecruiterCreateView.as_view(), name='create_recruiter'),
    path('recruiter/list/', RecruiterListView.as_view(), name='recruiter_list'),
    path('recruiter-details/<slug:slug>/', RecruiterDetailView.as_view(), name='recruiter_detail'),
    path('recruiter-delete/<slug:slug>/', RecruiterDeleteView.as_view(), name='recruiter_delete'),
    path('recruiter/<slug:slug>/update/', RecruiterUpdateView.as_view(), name='update_recruiter'),

]