from django import forms
from .models import UserProfile

class PersonalDataForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'birthday', 'address', 'want_resuscitate']
        widgets = {
            'birthday': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'want_resuscitate': 'I want to be resuscitate'
        }
