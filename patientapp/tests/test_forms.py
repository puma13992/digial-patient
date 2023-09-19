from django.test import TestCase
from patientapp.models import UserProfile, MediDisList, Doctor, Contact
from patientapp.forms import PersonalDataForm, MedicationListForm,\
    DoctorForm, ContactForm


# Test personal data form
class PersonalDataFormTests(TestCase):
    def test_personal_data_form_valid(self):
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'birthday': '1990-01-01',
            'address': '123 Main St, City',
            'want_resuscitate': True,
            'share': False,
        }
        form = PersonalDataForm(data=data)
        self.assertTrue(form.is_valid())

    def test_personal_data_form_invalid(self):
        data = {
            'first_name': '',  # Required field, should be non-empty
            'last_name': 'Doe',
            'birthday': 'invalid_date',  # Invalid date format
            'address': '123 Main St, City',
            'want_resuscitate': True,
            'share': False,
        }
        form = PersonalDataForm(data=data)
        self.assertFalse(form.is_valid())


# Test medication/diseases form
class MedicationListFormTests(TestCase):
    def test_medication_list_form_valid(self):
        data = {
            'medication_or_disease_name': 'Aspirin',
            'instructions': 'Take one tablet daily with water.',
        }
        form = MedicationListForm(data=data)
        self.assertTrue(form.is_valid())


# Test doctor form
class DoctorFormTests(TestCase):
    def test_doctor_form_valid(self):
        data = {
            'doctor_name': 'Dr. Smith',
            'details': 'Specializes in Cardiology',
        }
        form = DoctorForm(data=data)
        self.assertTrue(form.is_valid())


# Test contact form
class ContactFormTests(TestCase):
    def test_contact_form_valid(self):
        data = {
            'contact_name': 'Alice',
            'details': 'Friend',
        }
        form = ContactForm(data=data)
        self.assertTrue(form.is_valid())
