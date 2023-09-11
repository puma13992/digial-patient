from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import UserProfile, MediDisList
from .forms import PersonalDataForm, MedicationListForm


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


def medidis(request):
    if request.user.is_authenticated:
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)

        if request.method == 'POST':
            form = MedicationListForm(request.POST)
            if form.is_valid():
                medication_entry = form.save(commit=False)
                medication_entry.user_profile = user_profile
                medication_entry.save()
                messages.success(request, 'Your list has been successfully updated.')
                return redirect('medidis')
        else:
            form = MedicationListForm()

        medication_entries = MediDisList.objects.filter(user_profile=user_profile)

        return render(request, 'medidis.html', {'form': form, 'user_profile': user_profile, 'medication_entries': medication_entries})

    else:
        messages.error(request, 'You have to be logged in to show this page.')
        return redirect('../accounts/login/')


def edit_medidis(request, entry_id):
    entry = get_object_or_404(MediDisList, id=entry_id)

    if request.method == 'POST':
        form = MedicationListForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your list has been successfully updated.')
            return redirect('medidis')
    else:
        form = MedicationListForm(instance=entry)

    return render(request, 'edit_medidis.html', {'form': form, 'entry': entry})


def delete_medidis(request, entry_id):
    entry = get_object_or_404(MediDisList, id=entry_id)

    if request.method == 'POST':
        entry.delete()
        messages.success(request, 'Your entry has been successfully deleted.')
        return redirect('medidis')

    return render(request, 'delete_medidis.html', {'entry': entry})
