from django import forms
from .models import Club

class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ['name', 'description', 'image', 'quota']
