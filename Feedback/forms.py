from django import forms
from Feedback.models import FeedbackModel

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedbackModel
        fields = ('id', 'title', 'description', 'anonymous')