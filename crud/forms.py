from django import forms
from .models import Job, Recruiter

class JobCreateForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            'company_name', 'recruiter', 'requirements', 'job_position', 'job_link', 'apply_date', 'status'
        ]
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'recruiter': forms.Select(attrs={'class': 'form-control'}),
            'requirements': forms.Textarea(attrs={'class': 'form-control'}),
            'job_position': forms.TextInput(attrs={'class': 'form-control'}),
            'job_link': forms.URLInput(attrs={'class': 'form-control'}),
            'apply_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status' : forms.Select(attrs={'class':'form-control', 'type':'date'})
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields['recruiter'].queryset = Recruiter.objects.filter(user=user)

class JobUpdateForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            'company_name', 'recruiter', 'requirements', 'job_position', 'job_link', 'apply_date', 'status'
        ]
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'recruiter': forms.Select(attrs={'class': 'form-control'}),
            'requirements': forms.Textarea(attrs={'class': 'form-control'}),
            'job_position': forms.TextInput(attrs={'class': 'form-control'}),
            'job_link': forms.URLInput(attrs={'class': 'form-control'}),
            'apply_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status' : forms.Select(attrs={'class':'form-control', 'type':'date'})
        }

class RecruiterCreateForm(forms.ModelForm):
    class Meta:
        model = Recruiter
        fields = ['recruiters_name', 'recruiters_email'] 
        widgets = {
            'recruiters_name': forms.TextInput(attrs={'class': 'form-control'}),
            'recruiters_email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class RecruiterUpdateForm(forms.ModelForm):
    class Meta:
        model = Recruiter
        fields = ['recruiters_name', 'recruiters_email'] 
        widgets = {
            'recruiters_name': forms.TextInput(attrs={'class': 'form-control'}),
            'recruiters_email': forms.EmailInput(attrs={'class': 'form-control'}),
        }