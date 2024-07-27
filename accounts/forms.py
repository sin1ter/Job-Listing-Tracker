from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUserModel

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUserModel
        fields = ('email', 'phone', 'date_of_birth')

        widgets = {
            'email' : forms.EmailInput(attrs={'class': 'form-control'}), 
            'phone' : forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth' : forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUserModel
        fields = ('email', 'phone', 'date_of_birth', 'github', 'linkedin')

    
        widgets = {
                'email' : forms.EmailInput(attrs={'class': 'form-control'}), 
                'phone' : forms.TextInput(attrs={'class': 'form-control'}),
                'date_of_birth' : forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),

            }



class EditProfileForm(forms.ModelForm):
    
    class Meta:
        model = CustomUserModel
        fields = ['email', 'username', 'first_name', 'last_name', 'phone', 'date_of_birth', 'github', 'linkedin', 'resume']

        widgets = {
            'email' : forms.EmailInput(attrs={'class': 'form-control'}), 
            'username' : forms.TextInput(attrs={'class': 'form-control'}), 
            'first_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'last_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'phone' : forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth' : forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'github' : forms.URLInput(attrs={'class': 'form-control'}),
            'linkedin' : forms.URLInput(attrs={'class': 'form-control'}),
            'resume': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

       
