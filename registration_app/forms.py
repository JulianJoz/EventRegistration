# registration_app/forms.py

from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    SESSION_CHOICES = [
        ('session_1', 'Session 1'),
        ('session_2', 'Session 2'),
        ('session_3', 'Session 3'),
    ]

    full_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15)
    event_sessions = forms.ChoiceField(choices=SESSION_CHOICES, widget=forms.Select)

    class Meta:
        model = Registration
        fields = ['full_name', 'email', 'phone_number', 'event_sessions']

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number.isdigit():
            raise forms.ValidationError('Phone number should only contain numbers.')
        return phone_number
