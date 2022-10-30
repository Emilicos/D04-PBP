from django import forms
from Blogpost.models import BlogpostModel

class BlogpostForm(forms.ModelForm):
    LOW = "LW"
    INTERMEDIATE = "IM"
    HIGH = "HH"
    IMPORTANCE_CHOICES = [
        (LOW, 'Low'),
        (INTERMEDIATE, 'Intermediate'),
        (HIGH, 'High'),
    ]

    class Meta:
        model = BlogpostModel
        fields = ('id', 'title', 'opening', 'main', 'closing', 'importance')
        
        widgets = {
            "title": forms.TextInput(attrs = {"class": "form-control my-4", "name": "title", "placeholder": "Title", 'required': 'required', "id": "title"}),
            "opening": forms.Textarea(attrs = {"class": "form-control my-4", "name": "opening", "placeholder": "Opening", 'rows':0, 'cols':0, 'required': 'required', "id": "opening"}),
            "main": forms.Textarea(attrs = {"class": "form-control my-4", "name": "main", "placeholder": "Main", 'rows':0, 'cols':0, 'required': 'required', "id": "main"}),
            "closing": forms.Textarea(attrs = {"class": "form-control my-4", "name": "closing", "placeholder": "Closing", 'rows':0, 'cols':0, 'required': 'required', "id": "closing"}),
            "importance": forms.Select(attrs = {"class": "form-select my-4", "name": "importance", 'required': 'required', "id": "importance"})
        }