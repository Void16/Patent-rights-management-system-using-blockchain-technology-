from django import forms
from .models import Patent

class PatentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Patent
        fields = ['title', 'description', 'document']
