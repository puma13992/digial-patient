from django.contrib import admin
from .models import UserProfile, MediDisList, Doctor

admin.site.register(UserProfile)
admin.site.register(MediDisList)
admin.site.register(Doctor)
