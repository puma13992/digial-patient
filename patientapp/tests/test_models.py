from django.test import TestCase
from patientapp.models import UserProfile, MediDisList, Doctor, Contact
from django.contrib.auth.models import User
import datetime


# Test model UserProfile
class TestUserProfile(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.user_profile = UserProfile.objects.create(
            user=self.user,
            first_name='John',
            last_name='Doe',
            birthday=datetime.date(1990, 1, 1),
            address='123 Main St',
            want_resuscitate=True,
            share=False,
            public_link='https://example.com/johndoe'
        )

    def test_user_profile_str(self):
        self.assertEqual(str(self.user_profile), 'testuser')

    def test_user_profile_defaults(self):
        self.assertTrue(self.user_profile.want_resuscitate)
        self.assertFalse(self.user_profile.share)

    def test_user_profile_has_user(self):
        self.assertEqual(self.user_profile.user, self.user)

    def test_user_profile_has_birthday(self):
        self.assertEqual(self.user_profile.birthday, datetime.date(1990, 1, 1))


# Test model MediDisList
class TestMediDisList(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.user_profile = UserProfile.objects.create(user=self.user)
        self.medi_dis_list = MediDisList.objects.create(
            user_profile=self.user_profile,
            medication_or_disease_name='Medication 1',
            instructions='Take twice a day'
        )

    def test_medi_dis_list_str(self):
        self.assertEqual(str(self.medi_dis_list), 'testuser')

    def test_medi_dis_list_defaults(self):
        self.assertIsNotNone(self.medi_dis_list.instructions)
        self.assertEqual(self.medi_dis_list.instructions, 'Take twice a day')


# Test model Doctor
class TestDoctor(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.user_profile = UserProfile.objects.create(user=self.user)
        self.doctor = Doctor.objects.create(
            user_profile=self.user_profile,
            doctor_name='Dr. Smith',
            details='Cardiologist'
        )

    def test_doctor_str(self):
        self.assertEqual(str(self.doctor), 'testuser')

    def test_doctor_defaults(self):
        self.assertIsNotNone(self.doctor.details)
        self.assertEqual(self.doctor.details, 'Cardiologist')


# Test model Contact
class TestContact(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.user_profile = UserProfile.objects.create(user=self.user)
        self.contact = Contact.objects.create(
            user_profile=self.user_profile,
            contact_name='Emergency Contact',
            details='John Doe Sr.'
        )

    def test_contact_str(self):
        self.assertEqual(str(self.contact), 'testuser')

    def test_contact_defaults(self):
        self.assertIsNotNone(self.contact.details)
        self.assertEqual(self.contact.details, 'John Doe Sr.')
