from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.db.models import Count

from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import *
from accounts.models import CustomUserModel
from .forms import *

# Create your views here.

class JobListView(LoginRequiredMixin, ListView):
    model = Job
    template_name = 'job_list.html'
    context_object_name = 'jobs'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        return Job.objects.filter(user=self.request.user)

class JobDetailView(LoginRequiredMixin, DetailView):
    model = Job
    template_name = 'job_detail.html'
    context_object_name = 'job'
    login_url = reverse_lazy('login')

    def get_object(self):
        return Job.objects.get(slug=self.kwargs['slug'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        job = self.get_object()
        context['recruiter'] = job.recruiter
        return context

class JobCreateView(LoginRequiredMixin, CreateView):
    model = Job
    form_class = JobCreateForm
    template_name = 'job_create.html'
    success_url = reverse_lazy("job_list")
    login_url = reverse_lazy('login')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class JobUpdateView(LoginRequiredMixin, UpdateView):
    model = Job
    form_class = JobUpdateForm
    template_name = 'job_update.html'
    context_object_name = 'job'
    success_url = reverse_lazy('job_list')
    login_url = reverse_lazy('login')

    def get_queryset(self):
        return Job.objects.filter(user=self.request.user)
    

class JobDeleteView(LoginRequiredMixin, DeleteView):
    model = Job
    template_name = 'job_confirm_delete.html'
    success_url = reverse_lazy("job_list")
    login_url = reverse_lazy('login')

    def get_queryset(self):
        return Job.objects.filter(user=self.request.user)
    

class RecruiterCreateView(LoginRequiredMixin, CreateView):
    model = Recruiter
    template_name = 'recruiter_create.html'
    form_class = RecruiterCreateForm
    success_url = reverse_lazy("job_list")
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class RecruiterListView(LoginRequiredMixin, ListView):
    model = Recruiter
    template_name = 'recruiter_list_view.html'
    context_object_name = 'recruiters'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        return Recruiter.objects.filter(user=self.request.user)
    
class RecruiterDetailView(LoginRequiredMixin, DetailView):
    model = Recruiter
    template_name = 'recruiter_detail_view.html'
    context_object_name = 'recruiter'
    login_url = reverse_lazy('login')

    def get_object(self):
        return Recruiter.objects.get(slug=self.kwargs['slug'])
    
class RecruiterDeleteView(LoginRequiredMixin, DeleteView):
    model = Recruiter
    template_name = 'recruiter_confirm_delete.html'
    success_url = reverse_lazy('recruiter_list')
    login_url = reverse_lazy('login')

    def get_queryset(self):
        return Recruiter.objects.filter(user=self.request.user)
    
class RecruiterUpdateView(LoginRequiredMixin, UpdateView):
    model = Recruiter
    form_class = RecruiterUpdateForm
    template_name = 'recruiter_update.html'
    context_object_name = 'recruiter'
    success_url = reverse_lazy('recruiter_list')
    login_url = reverse_lazy('login')

    def get_queryset(self):
        return Recruiter.objects.filter(user=self.request.user)
    
def dashboard(request):
    
    if not request.user.is_authenticated:
        return redirect('login') 


    job_counts = Job.objects.filter(user=request.user).values('status').annotate(count=Count('status'))
    all_jobs = Job.objects.filter(user=request.user).all().count()
    accepted = Job.objects.filter(user=request.user).filter(status='Accepted').count()
    ghosted = Job.objects.filter(user=request.user).filter(status='Ghosted').count()
    rejected = Job.objects.filter(user=request.user).filter(status='Rejected').count()
    pending = Job.objects.filter(user=request.user).filter(status='Pending').count()
    replied = Job.objects.filter(user=request.user).filter(status='Replied').count()

    statuses = [item['status'] for item in job_counts] 
    counts = [item['count'] for item in job_counts]

    context = {
        'statuses': statuses,
        'counts': counts, 
        'all_jobs' : all_jobs,
        'accepted' : accepted,
        'ghosted' : ghosted,
        'rejected' : rejected,
        'pending' : pending, 
        'replied' : replied,
    }

    return render(request, 'registration/dashboard.html', context)
