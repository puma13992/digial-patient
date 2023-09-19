from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.messages import get_messages
from patientapp.models import UserProfile, MediDisList, Doctor, Contact
from django.http import HttpResponseNotFound
from patientapp.views import custom_404


# Set up basic
class BaseTestCase(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(
            username=self.username, password=self.password
            )
        self.user_profile = UserProfile.objects.create(user=self.user)


# Test home view
class HomeViewTestCase(BaseTestCase):
    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


# Test profile view
class ProfileViewTestCase(BaseTestCase):
    def test_profile_view_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')

    def test_profile_view_unauthenticated(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/')


# Test view personal data view
class ViewPersonalDataTestCase(BaseTestCase):

    def test_view_personal_data_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('personal_data'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'personal_data.html')

    def test_view_personal_data_unauthenticated(self):
        response = self.client.get(reverse('personal_data'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/')


# Test edit personal data view
class EditPersonalDataViewTestCase(BaseTestCase):

    def test_edit_personal_data_view_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('edit_personal_data'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_personal_data.html')

    def test_edit_personal_data_view_unauthenticated(self):
        response = self.client.get(reverse('edit_personal_data'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/')


# Test medidis view
class MedidisViewTestCase(BaseTestCase):

    def test_medidis_view_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('medidis'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'medidis.html')

    def test_medidis_view_unauthenticated(self):
        response = self.client.get(reverse('medidis'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/')


# Test edit medidis view
class EditMedidisViewTestCase(BaseTestCase):

    def test_edit_medidis_view_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        medication_entry = MediDisList.objects.create(
            user_profile=self.user_profile,
            medication_or_disease_name='Test Medication'
            )
        response = self.client.get(
            reverse('edit_medidis', args=[medication_entry.id])
            )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_medidis.html')

    def test_edit_medidis_not_authenticated(self):
        entry_id = 1
        response = self.client.get(reverse('edit_medidis', args=[entry_id]))

        self.assertEqual(response.status_code, 302)

        expected_url = (
            '/accounts/login' +
            f'?next={reverse("edit_medidis", args=[entry_id])}'
            )
        self.assertEqual(response.url, expected_url)

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]), 'You have to be logged in to show this page.'
            )


# Test delete medidis view
class DeleteMedidisViewTestCase(BaseTestCase):

    def test_delete_medidis_view_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        medication_entry = MediDisList.objects.create(
            user_profile=self.user_profile,
            medication_or_disease_name='Test Medication'
            )
        response = self.client.get(
            reverse('delete_medidis', args=[medication_entry.id])
            )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_medidis.html')

    def test_redirect_if_not_authenticated(self):
        entry_id = 1
        response = self.client.get(reverse('delete_medidis', args=[entry_id]))

        self.assertEqual(response.status_code, 302)

        expected_url = (
            '/accounts/login' +
            f'?next={reverse("delete_medidis", args=[entry_id])}'
            )
        self.assertEqual(response.url, expected_url)

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]), 'You have to be logged in to show this page.'
            )


# Test doctor view
class DoctorViewTestCase(BaseTestCase):

    def test_doctor_view_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('doctor'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctor.html')

    def test_doctor_view_unauthenticated(self):
        response = self.client.get(reverse('doctor'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/')


# Test edit doctor view
class EditDoctorViewTestCase(BaseTestCase):

    def test_edit_doctor_view_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        doctor_entry = Doctor.objects.create(
            user_profile=self.user_profile, doctor_name='Test Doctor'
            )
        response = self.client.get(
            reverse('edit_doctor', args=[doctor_entry.id])
            )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_doctor.html')

    def test_edit_doctor_not_authenticated(self):
        entry_id = 1
        response = self.client.get(reverse('edit_doctor', args=[entry_id]))

        self.assertEqual(response.status_code, 302)

        expected_url = (
            '/accounts/login' +
            f'?next={reverse("edit_doctor", args=[entry_id])}'
            )
        self.assertEqual(response.url, expected_url)

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]), 'You have to be logged in to show this page.'
            )


# Test delete doctor view
class DeleteDoctorViewTestCase(BaseTestCase):

    def test_delete_doctor_view_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        doctor_entry = Doctor.objects.create(
            user_profile=self.user_profile, doctor_name='Test Doctor'
            )
        response = self.client.get(
            reverse('delete_doctor', args=[doctor_entry.id])
            )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_doctor.html')

    def test_delete_doctor_not_authenticated(self):
        entry_id = 1
        response = self.client.get(reverse('delete_doctor', args=[entry_id]))

        self.assertEqual(response.status_code, 302)

        expected_url = (
            '/accounts/login' +
            f'?next={reverse("delete_doctor", args=[entry_id])}'
            )
        self.assertEqual(response.url, expected_url)

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]), 'You have to be logged in to show this page.'
            )


# Test contact view
class ContactViewTestCase(BaseTestCase):

    def test_contact_view_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_contact_view_unauthenticated(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/')


# Test edit contact view
class EditContactViewTestCase(BaseTestCase):

    def test_edit_contact_view_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        contact_entry = Contact.objects.create(
            user_profile=self.user_profile, contact_name='Test Contact'
            )
        response = self.client.get(
            reverse('edit_contact', args=[contact_entry.id])
            )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_contact.html')

    def test_edit_contact_not_authenticated(self):
        entry_id = 1
        response = self.client.get(reverse('edit_contact', args=[entry_id]))

        self.assertEqual(response.status_code, 302)

        expected_url = (
            '/accounts/login' +
            f'?next={reverse("edit_contact", args=[entry_id])}'
            )
        self.assertEqual(response.url, expected_url)

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]), 'You have to be logged in to show this page.'
            )


# Test delete contact view
class DeleteContactViewTestCase(BaseTestCase):

    def test_delete_contact_view_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        contact_entry = Contact.objects.create(
            user_profile=self.user_profile, contact_name='Test Contact'
            )
        response = self.client.get(
            reverse('delete_contact', args=[contact_entry.id])
            )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_contact.html')

    def test_delete_contact_not_authenticated(self):
        entry_id = 1
        response = self.client.get(reverse('delete_contact', args=[entry_id]))

        self.assertEqual(response.status_code, 302)

        expected_url = (
            '/accounts/login' +
            f'?next={reverse("delete_contact", args=[entry_id])}'
            )
        self.assertEqual(response.url, expected_url)

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]), 'You have to be logged in to show this page.'
            )


# Test delete account view
class DeleteAccountViewTestCase(BaseTestCase):

    def test_delete_account_authenticated_correct_password(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.post(
            reverse('delete_account'), {'password': self.password}
            )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        user = authenticate(username=self.username, password=self.password)
        self.assertIsNone(user)
        self.assertFalse(User.objects.filter(username=self.username).exists())

    def test_delete_account_authenticated_wrong_password(self):
        self.client.login(username=self.username, password=self.password)
        wrong_password = 'wrongpassword'
        response = self.client.post(
            reverse('delete_account'), {'password': wrong_password}
            )
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response, 'Password is invalid. Your account has not been deleted.'
            )

    def test_delete_account_unauthenticated(self):
        response = self.client.post(
            reverse('delete_account'), {'password': self.password}
            )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/')


# Test 404 view
class Custom404TestCase(TestCase):
    def test_custom_404_view(self):
        response = self.client.get('/nonexistentpage/')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')
