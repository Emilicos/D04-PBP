from django import forms
from .models import Appointment
from Authentication.models import User

class AppointmentForm(forms.ModelForm):
    date = forms.DateInput()
    time = forms.TimeInput()
    doctor = forms.ModelChoiceField(queryset=User.objects.filter(role = 2), widget=forms.Select(attrs={'class': 'form-control', 'id': 'post-doctor'}), empty_label='Select a Doctor', to_field_name='username')
    class Meta:
        model = Appointment
        fields = ('date', 'time', 'doctor')
        widgets = {
            'date': forms.DateInput(
                format = ('%Y-%m-%d'),
                attrs = {'class': 'form-control', 'type': 'date', 'id': 'post-date'}),
            'time': forms.TimeInput(
                format = ('%H:%M'),
                attrs = {'class': 'form-control', 'type': 'time', 'id': 'post-time'}),
        }