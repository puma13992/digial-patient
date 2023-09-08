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

    def __str__(self):
        return self.user.username
