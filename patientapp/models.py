from django.db import models
from django.contrib.auth.models import User

# Personal data
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    birthday = models.DateField(null=True)
    address = models.TextField(null=True)
    want_resuscitate = models.BooleanField(default=True)
    share = models.BooleanField(default=False)
    public_link = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.user.username


# Medications, diseases
class MediDisList(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    medication_or_disease_name = models.CharField(max_length=200, null=True)
    instructions = models.CharField(max_length=200, null=True, blank=True)


    def __str__(self):
        return self.user_profile.user.username


# Doctors
class Doctor(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    doctor_name = models.CharField(max_length=200, null=True)
    details = models.CharField(max_length=200, null=True, blank=True)


    def __str__(self):
        return self.user_profile.user.username


# Contact
class Contact(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    contact_name = models.CharField(max_length=200, null=True)
    details = models.CharField(max_length=200, null=True, blank=True)


    def __str__(self):
        return self.user_profile.user.username
