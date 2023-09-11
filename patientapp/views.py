from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import UserProfile, MediDisList, Doctor, Contact
from .forms import PersonalDataForm, MedicationListForm, DoctorForm, ContactForm


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


def doctor(request):
    if request.user.is_authenticated:
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)

        if request.method == 'POST':
            form = DoctorForm(request.POST)
            if form.is_valid():
                doctor_entry = form.save(commit=False)
                doctor_entry.user_profile = user_profile
                doctor_entry.save()
                messages.success(request, 'Your list has been successfully updated.')
                return redirect('doctor')
        else:
            form = DoctorForm()

        doctor_entries = Doctor.objects.filter(user_profile=user_profile)

        return render(request, 'doctor.html', {'form': form, 'user_profile': user_profile, 'doctor_entries': doctor_entries})

    else:
        messages.error(request, 'You have to be logged in to show this page.')
        return redirect('../accounts/login/')


def edit_doctor(request, entry_id):
    entry = get_object_or_404(Doctor, id=entry_id)

    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your list has been successfully updated.')
            return redirect('doctor')
    else:
        form = DoctorForm(instance=entry)

    return render(request, 'edit_doctor.html', {'form': form, 'entry': entry})


def delete_doctor(request, entry_id):
    entry = get_object_or_404(Doctor, id=entry_id)

    if request.method == 'POST':
        entry.delete()
        messages.success(request, 'Your entry has been successfully deleted.')
        return redirect('doctor')

    return render(request, 'delete_doctor.html', {'entry': entry})


def contact(request):
    if request.user.is_authenticated:
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)

        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                contact_entry = form.save(commit=False)
                contact_entry.user_profile = user_profile
                contact_entry.save()
                messages.success(request, 'Your list has been successfully updated.')
                return redirect('contact')
        else:
            form = ContactForm()

        contact_entries = Contact.objects.filter(user_profile=user_profile)

        return render(request, 'contact.html', {'form': form, 'user_profile': user_profile, 'contact_entries': contact_entries})

    else:
        messages.error(request, 'You have to be logged in to show this page.')
        return redirect('../accounts/login/')


def edit_contact(request, entry_id):
    entry = get_object_or_404(Contact, id=entry_id)

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your list has been successfully updated.')
            return redirect('contact')
    else:
        form = ContactForm(instance=entry)

    return render(request, 'edit_contact.html', {'form': form, 'entry': entry})


def delete_contact(request, entry_id):
    entry = get_object_or_404(Contact, id=entry_id)

    if request.method == 'POST':
        entry.delete()
        messages.success(request, 'Your entry has been successfully deleted.')
        return redirect('contact')

    return render(request, 'delete_contact.html', {'entry': entry})


# custom 404 view
def custom_404(request, exception):
    return render(request, '404.html', status=404)
