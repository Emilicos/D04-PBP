from django import forms
from .models import *

class ExperienceForm(forms.ModelForm):
    title= forms.CharField(widget= forms.TextInput())
    experience= forms.CharField(widget=forms.Textarea(attrs={'style': 'width: 15em;'}))

    class Meta:
        model = Experience
        fields = ('id','title', 'experience')