from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import CustomUser, VideoIdea , ResourceLink

class CustomUserRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'email', 'age', 'institute', 'main_platform']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control mb-3'

class VideoIdeaForm(forms.ModelForm):
    class Meta:
        model = VideoIdea
        fields = ['title', 'description', 'status', 'target_date']
        
        widgets = {
            'target_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control mb-3'
            
        self.fields['status'].widget.attrs['class'] = 'form-select mb-3'

class ResourceLinkForm(forms.ModelForm):
    class Meta:
        model = ResourceLink
        fields = ['title', 'url']
        
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'e.g., Python Docs, B-Roll Video'}),
            'url': forms.URLInput(attrs={'placeholder': 'https://...'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control mb-3'