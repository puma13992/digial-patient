from django import forms
from .models import UserProfile, MediDisList, Doctor, Contact


class PersonalDataForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'birthday', 'address', 'want_resuscitate', 'share']
        widgets = {
            'birthday': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'want_resuscitate': 'I want to be resuscitate',
            'share': 'I want to share my account'
        }


class MedicationListForm(forms.ModelForm):
    class Meta:
        model = MediDisList
        fields = ['medication_or_disease_name', 'instructions']


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['doctor_name', 'details']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['contact_name', 'details']
