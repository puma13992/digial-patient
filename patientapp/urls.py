from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("profile/", views.profile, name="profile"),
    path('edit_personal_data/', views.edit_personal_data, name='edit_personal_data'),
    path('personal_data/', views.view_personal_data, name='personal_data'),
]
