from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.shortcuts import get_object_or_404
from patientapp.models import UserProfile, MediDisList, Doctor, Contact
from patientapp.forms import MedicationListForm, ContactForm, DoctorForm,\
    PersonalDataForm


# View personal data form
class PersonalDataFormTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
            )

    def test_personal_data_form_save_with_user(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'birthday': '1990-01-01',
            'address': '123 Main St, City',
            'want_resuscitate': True,
            'share': False,
        }

        user_profile = UserProfile.objects.create(user=self.user)

        form = PersonalDataForm(data=form_data, instance=user_profile)

        self.assertTrue(form.is_valid())
        form.save()

        user_profile.refresh_from_db()

        self.assertEqual(user_profile.first_name, 'John')
        self.assertEqual(user_profile.last_name, 'Doe')
        self.assertEqual(
            user_profile.birthday.strftime('%Y-%m-%d'), '1990-01-01'
            )
        self.assertEqual(user_profile.address, '123 Main St, City')
        self.assertTrue(user_profile.want_resuscitate)
        self.assertFalse(user_profile.share)


# View functionality medidis form
class MedidisViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
            )
        self.client.login(username='testuser', password='testpassword')
        self.user_profile, _ = UserProfile.objects.get_or_create(
            user=self.user
            )
        self.url = reverse('medidis')

    def test_medication_entry_creation(self):
        response = self.client.post(
            self.url, {'medication_or_disease_name': 'Medication Name'}
            )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(MediDisList.objects.count(), 1)
        medication_entry = MediDisList.objects.first()
        self.assertEqual(
            medication_entry.medication_or_disease_name, 'Medication Name'
            )
        self.assertEqual(medication_entry.user_profile, self.user_profile)

    def test_invalid_medication_entry(self):
        response = self.client.post(self.url, {})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(MediDisList.objects.count(), 0)
        self.assertFormError(
            response, 'form', 'medication_or_disease_name',
            'This field is required.'
            )


# Edit functionality medidis form
class EditMedidisViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
            )
        self.entry = MediDisList.objects.create(
            medication_or_disease_name='Test Entry',
            instructions='Test Description',
            user_profile_id=self.user.id,
        )
        self.url = reverse('edit_medidis', args=[self.entry.id])

    def test_edit_medidis_authenticated_user(self):
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_medidis.html')

        form = response.context['form']
        self.assertIsInstance(form, MedicationListForm)

        form_data = {
            'medication_or_disease_name': 'Updated Name',
            'instructions': 'Updated Description',
        }
        response = self.client.post(self.url, form_data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('medidis'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]), 'Your list has been successfully updated.'
            )


# Delete functionality medidis form
class DeleteMedidisViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
            )

        self.user_profile = UserProfile.objects.create(user=self.user)
        self.entry = MediDisList.objects.create(
            user_profile=self.user_profile,
            medication_or_disease_name='Test Entry',
            instructions='Test Description',
        )

    def test_delete_medidis_view(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('delete_medidis', args=[self.entry.id])
        response = self.client.post(url)
        self.assertRedirects(response, reverse('medidis'))
        self.assertFalse(MediDisList.objects.filter(id=self.entry.id).exists())
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]), 'Your entry has been successfully deleted.'
            )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


# View functionality doctor form
class DoctorViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
            )
        self.client.login(username='testuser', password='testpassword')
        self.user_profile, _ = UserProfile.objects.get_or_create(
            user=self.user
            )
        self.url = reverse('doctor')

    def test_doctor_entry_creation(self):
        response = self.client.post(self.url, {'doctor_name': 'Doctor Name'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Doctor.objects.count(), 1)
        doctor_entry = Doctor.objects.first()
        self.assertEqual(doctor_entry.doctor_name, 'Doctor Name')
        self.assertEqual(doctor_entry.user_profile, self.user_profile)

    def test_invalid_doctor_entry(self):
        response = self.client.post(self.url, {})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Doctor.objects.count(), 0)
        self.assertFormError(
            response, 'form', 'doctor_name', 'This field is required.'
            )


# Edit functionality doctor form
class EditDoctorViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
            )
        self.user_profile = UserProfile.objects.create(user=self.user)
        self.doctor = Doctor.objects.create(
            doctor_name='Test Doctor',
            details='Test Specialty',
            user_profile=self.user_profile,
        )
        self.url = reverse('edit_doctor', args=[self.doctor.id])

    def test_edit_doctor_authenticated_user(self):
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_doctor.html')

        form = response.context['form']
        self.assertIsInstance(form, DoctorForm)

        form_data = {
            'doctor_name': 'Updated Name',
            'details': 'Updated Specialty',
        }
        response = self.client.post(self.url, form_data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('doctor'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]), 'Your list has been successfully updated.'
            )


# Delete functionality doctor form
class DeleteDoctorViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
            )

        self.user_profile = UserProfile.objects.create(user=self.user)
        self.entry = Doctor.objects.create(
            user_profile=self.user_profile,
            doctor_name='Test Entry',
            details='Test Description',
        )

    def test_delete_doctor_view(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('delete_doctor', args=[self.entry.id])
        response = self.client.post(url)
        self.assertRedirects(response, reverse('doctor'))
        self.assertFalse(Doctor.objects.filter(id=self.entry.id).exists())
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]), 'Your entry has been successfully deleted.'
            )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


# View functionality contact form
class ContactViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
            )
        self.client.login(username='testuser', password='testpassword')
        self.user_profile, _ = UserProfile.objects.get_or_create(
            user=self.user
            )
        self.url = reverse('contact')

    def test_contact_entry_creation(self):
        response = self.client.post(self.url, {'contact_name': 'Contact Name'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Contact.objects.count(), 1)
        contact_entry = Contact.objects.first()
        self.assertEqual(contact_entry.contact_name, 'Contact Name')
        self.assertEqual(contact_entry.user_profile, self.user_profile)

    def test_invalid_contact_entry(self):
        response = self.client.post(self.url, {})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Contact.objects.count(), 0)
        self.assertFormError(
            response, 'form', 'contact_name', 'This field is required.'
            )


# Edit contact form
class EditContactViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
            )
        self.user_profile = UserProfile.objects.create(user=self.user)
        self.contact = Contact.objects.create(
            contact_name='Test Contact',
            details='test@example.com',
            user_profile=self.user_profile,
        )
        self.url = reverse('edit_contact', args=[self.contact.id])

    def test_edit_contact_authenticated_user(self):
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_contact.html')

        form = response.context['form']
        self.assertIsInstance(form, ContactForm)

        form_data = {
            'contact_name': 'Updated Name',
            'details': 'updated@example.com',
        }
        response = self.client.post(self.url, form_data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('contact'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]), 'Your list has been successfully updated.'
            )


# Delete functionality contact form
class DeleteContactViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
            )

        self.user_profile = UserProfile.objects.create(user=self.user)
        self.entry = Contact.objects.create(
            user_profile=self.user_profile,
            contact_name='Test Entry',
            details='Test Description',
        )

    def test_delete_contact_view(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('delete_contact', args=[self.entry.id])
        response = self.client.post(url)
        self.assertRedirects(response, reverse('contact'))
        self.assertFalse(Contact.objects.filter(id=self.entry.id).exists())
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]), 'Your entry has been successfully deleted.'
            )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
