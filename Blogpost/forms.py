from django import forms
from Blogpost.models import BlogpostModel

class BlogpostForm(forms.ModelForm):
    class Meta:
        model = BlogpostModel
        fields = ('id', 'title', 'opening', 'main', 'closing', 'importance')