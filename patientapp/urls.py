from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("profile/", views.profile, name="profile"),
    path('edit_personal_data/', views.edit_personal_data, name='edit_personal_data'),
    path('personal_data/', views.view_personal_data, name='personal_data'),
    path('medidis/', views.medidis, name='medidis'),
    path('medidis/edit/<int:entry_id>/', views.edit_medidis, name='edit_medidis'),
    path('medidis/delete/<int:entry_id>/', views.delete_medidis, name='delete_medidis'),
    path('doctor/', views.doctor, name='doctor'),
    path('doctor/edit/<int:entry_id>/', views.edit_doctor, name='edit_doctor'),
    path('doctor/delete/<int:entry_id>/', views.delete_doctor, name='delete_doctor'),
    path('contact/', views.contact, name='contact'),
    path('contact/edit/<int:entry_id>/', views.edit_contact, name='edit_contact'),
]

handler404 = 'patientapp.views.custom_404'
