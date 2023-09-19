from django.test import TestCase
from django.urls import reverse, resolve
from patientapp import views


# Test home url
class TestHomeURL(TestCase):
    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, views.home)


# Test profile url
class TestProfileURL(TestCase):
    def test_profile_url_resolves(self):
        url = reverse('profile')
        self.assertEqual(resolve(url).func, views.profile)


# Test view personal data url
class TestViewPersonalDataURL(TestCase):
    def test_view_personal_data_url_resolves(self):
        url = reverse('personal_data')
        self.assertEqual(resolve(url).func, views.view_personal_data)


# Test edit personal data url
class TestEditPersonalDataURL(TestCase):
    def test_edit_personal_data_url_resolves(self):
        url = reverse('edit_personal_data')
        self.assertEqual(resolve(url).func, views.edit_personal_data)


# Test view medidis url
class TestMediDisURL(TestCase):
    def test_medidis_url_resolves(self):
        url = reverse('medidis')
        self.assertEqual(resolve(url).func, views.medidis)


# Test edit medidis url
class TestEditMediDisURL(TestCase):
    def test_edit_medidis_url_resolves(self):
        url = reverse('edit_medidis', args=[1])
        self.assertEqual(resolve(url).func, views.edit_medidis)


# Test delete medidis url
class TestDeleteMediDisURL(TestCase):
    def test_delete_medidis_url_resolves(self):
        url = reverse('delete_medidis', args=[1])
        self.assertEqual(resolve(url).func, views.delete_medidis)


# Test view doctor url
class TestDoctorURL(TestCase):
    def test_doctor_url_resolves(self):
        url = reverse('doctor')
        self.assertEqual(resolve(url).func, views.doctor)


# Test edit doctor url
class TestEditDoctorURL(TestCase):
    def test_edit_doctor_url_resolves(self):
        url = reverse('edit_doctor', args=[1])
        self.assertEqual(resolve(url).func, views.edit_doctor)


# Test delete doctor url
class TestDeleteDoctorURL(TestCase):
    def test_delete_doctor_url_resolves(self):
        url = reverse('delete_doctor', args=[1])
        self.assertEqual(resolve(url).func, views.delete_doctor)


# Test view contact url
class TestContactURL(TestCase):
    def test_contact_url_resolves(self):
        url = reverse('contact')
        self.assertEqual(resolve(url).func, views.contact)


# Test edit contact url
class TestEditContactURL(TestCase):
    def test_edit_contact_url_resolves(self):
        url = reverse('edit_contact', args=[1])
        self.assertEqual(resolve(url).func, views.edit_contact)


# Test delete contact url
class TestDeleteContactURL(TestCase):
    def test_delete_contact_url_resolves(self):
        url = reverse('delete_contact', args=[1])
        self.assertEqual(resolve(url).func, views.delete_contact)


# Test delete account url
class TestDeleteAccountURL(TestCase):
    def test_delete_account_url_resolves(self):
        url = reverse('delete_account')
        self.assertEqual(resolve(url).func, views.delete_account)
