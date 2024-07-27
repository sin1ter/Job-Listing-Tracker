from django import forms

from .models import Track, Resources

class TrackCreateForm(forms.ModelForm):
    
    class Meta:
        model = Track
        fields = ("title",)


class TrackUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Track
        fields = ("title",)

class ResourceCreateForm(forms.ModelForm):

    class Meta:
        model = Resources
        fields = ("title", "resources")
        