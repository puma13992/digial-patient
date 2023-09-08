from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserProfile
from .forms import PersonalDataForm


def home(request):
    return render(request, 'index.html')


def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        messages.error(request, 'You have to be logged in to show this page.')
        return redirect('../accounts/login/')


def edit_personal_data(request):
    if request.user.is_authenticated:
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)

        if request.method == 'POST':
            form = PersonalDataForm(request.POST, instance=user_profile)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your personal data has been successfully updated.')
                return redirect('personal_data')
        else:
            form = PersonalDataForm(instance=user_profile)

        return render(request, 'edit_personal_data.html', {'form': form})

    else:
        messages.error(request, 'You have to be logged in to show this page.')
        return redirect('../accounts/login/')


def view_personal_data(request):
    if request.user.is_authenticated:
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)
        return render(request, 'personal_data.html', {'user_profile': user_profile})  
    else:
        messages.error(request, 'You have to be logged in to show this page.')
        return redirect('../accounts/login/')
