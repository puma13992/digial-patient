from django.contrib import admin
from .models import UserProfile, MediDisList, Doctor, Contact

admin.site.register(UserProfile)
admin.site.register(MediDisList)
admin.site.register(Doctor)
admin.site.register(Contact)
