from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import logout
from .models import UserProfile, MediDisList, Doctor, Contact
from .forms import PersonalDataForm, MedicationListForm,\
    DoctorForm, ContactForm
from django.utils.crypto import get_random_string
from django.http import HttpResponseRedirect
from django.urls import reverse


# Home view
def home(request):
    return render(request, 'index.html')


# Profile view
def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        messages.error(request, 'You have to be logged in to show this page.')
        return redirect('../accounts/login/')


# Edit personal view
def edit_personal_data(request):
    if request.user.is_authenticated:
        user_profile, created = UserProfile.objects.get_or_create(
            user=request.user
            )
        form_personal_data = PersonalDataForm(instance=user_profile)
        public_link = user_profile.public_link

        if request.method == 'POST':
            form = PersonalDataForm(request.POST, instance=user_profile)
            if form.is_valid():
                if 'share' in form.changed_data and user_profile.share:
                    public_link = f"shared_link_{get_random_string()}"
                    user_profile.public_link = public_link
                elif 'share' in form.changed_data and not user_profile.share:
                    # Set public_link to None if 'share' is changed to 'no'
                    user_profile.public_link = None

                user_profile.save()
                messages.success(
                    request,
                    'Your personal data has been successfully updated.'
                    )
                return redirect('personal_data')
        else:
            form = PersonalDataForm(instance=user_profile)

        return render(
            request, 'edit_personal_data.html', {
                'form': form, 'public_link': public_link
                })

    else:
        messages.error(request, 'You have to be logged in to show this page.')
        return redirect('../accounts/login/')


# Show personal data view
def view_personal_data(request):
    if request.user.is_authenticated:
        user_profile, created = UserProfile.objects.get_or_create(
            user=request.user
            )
        public_link = user_profile.public_link
        return render(
            request, 'personal_data.html', {
                'user_profile': user_profile, 'public_link': public_link
                })

    else:
        messages.error(request, 'You have to be logged in to show this page.')
        return redirect('../accounts/login/')


# Show medication/diseases view
def medidis(request):
    if request.user.is_authenticated:
        user_profile, created = UserProfile.objects.get_or_create(
            user=request.user
            )

        if request.method == 'POST':
            form = MedicationListForm(request.POST)
            if form.is_valid():
                medication_entry = form.save(commit=False)
                medication_entry.user_profile = user_profile
                medication_entry.save()
                messages.success(
                    request, 'Your list has been successfully updated.'
                    )
                form = MedicationListForm()
        else:
            form = MedicationListForm()

        medication_entries = MediDisList.objects.filter(
            user_profile=user_profile
            )

        return render(
            request, 'medidis.html', {
                'form': form, 'user_profile': user_profile,
                'medication_entries': medication_entries
                })

    else:
        messages.error(request, 'You have to be logged in to show this page.')
        return redirect('../accounts/login/')


# Show edit medication/diseases view
def edit_medidis(request, entry_id):
    if request.user.is_authenticated:
        entry = get_object_or_404(MediDisList, id=entry_id)

        if request.method == 'POST':
            form = MedicationListForm(request.POST, instance=entry)
            if form.is_valid():
                form.save()
                messages.success(
                    request, 'Your list has been successfully updated.'
                    )
                return redirect('medidis')
        else:
            form = MedicationListForm(instance=entry)

        return render(
            request, 'edit_medidis.html', {'form': form, 'entry': entry}
            )
    else:
        messages.error(request, 'You have to be logged in to show this page.')
        next_url = reverse('edit_medidis', args=[entry_id])
        login_url = '/accounts/login' + f'?next={next_url}'
        return HttpResponseRedirect(login_url)


# Delete medication/diseases view
def delete_medidis(request, entry_id):
    if request.user.is_authenticated:
        entry = get_object_or_404(MediDisList, id=entry_id)

        if request.method == 'POST':
            entry.delete()
            messages.success(
                request, 'Your entry has been successfully deleted.'
                )
            return redirect('medidis')

        return render(request, 'delete_medidis.html', {'entry': entry})
    else:
        messages.error(request, 'You have to be logged in to show this page.')
        next_url = reverse('delete_medidis', args=[entry_id])
        login_url = '/accounts/login' + f'?next={next_url}'
        return HttpResponseRedirect(login_url)


# Show doctors view
def doctor(request):
    if request.user.is_authenticated:
        user_profile, created = UserProfile.objects.get_or_create(
            user=request.user
            )

        if request.method == 'POST':
            form = DoctorForm(request.POST)
            if form.is_valid():
                doctor_entry = form.save(commit=False)
                doctor_entry.user_profile = user_profile
                doctor_entry.save()
                messages.success(
                    request, 'Your list has been successfully updated.'
                    )
                form = DoctorForm()
        else:
            form = DoctorForm()

        doctor_entries = Doctor.objects.filter(user_profile=user_profile)

        return render(
            request, 'doctor.html', {
                'form': form, 'user_profile': user_profile,
                'doctor_entries': doctor_entries
                })

    else:
        messages.error(request, 'You have to be logged in to show this page.')
        return redirect('../accounts/login/')


# Edit doctors view
def edit_doctor(request, entry_id):
    if request.user.is_authenticated:
        entry = get_object_or_404(Doctor, id=entry_id)

        if request.method == 'POST':
            form = DoctorForm(request.POST, instance=entry)
            if form.is_valid():
                form.save()
                messages.success(
                    request, 'Your list has been successfully updated.'
                    )
                return redirect('doctor')
        else:
            form = DoctorForm(instance=entry)

        return render(
            request, 'edit_doctor.html', {'form': form, 'entry': entry}
            )
    else:
        messages.error(request, 'You have to be logged in to show this page.')
        next_url = reverse('edit_doctor', args=[entry_id])
        login_url = '/accounts/login' + f'?next={next_url}'
        return HttpResponseRedirect(login_url)


# Delete doctors view
def delete_doctor(request, entry_id):
    if request.user.is_authenticated:
        entry = get_object_or_404(Doctor, id=entry_id)

        if request.method == 'POST':
            entry.delete()
            messages.success(
                request, 'Your entry has been successfully deleted.'
                )
            return redirect('doctor')

        return render(request, 'delete_doctor.html', {'entry': entry})
    else:
        messages.error(request, 'You have to be logged in to show this page.')
        next_url = reverse('delete_doctor', args=[entry_id])
        login_url = '/accounts/login' + f'?next={next_url}'
        return HttpResponseRedirect(login_url)


# Show contacts view
def contact(request):
    if request.user.is_authenticated:
        user_profile, created = UserProfile.objects.get_or_create(
            user=request.user
            )

        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                contact_entry = form.save(commit=False)
                contact_entry.user_profile = user_profile
                contact_entry.save()
                messages.success(
                    request, 'Your list has been successfully updated.'
                    )
                form = ContactForm()
        else:
            form = ContactForm()

        contact_entries = Contact.objects.filter(user_profile=user_profile)

        return render(
            request, 'contact.html', {
                'form': form, 'user_profile': user_profile,
                'contact_entries': contact_entries
                })

    else:
        messages.error(request, 'You have to be logged in to show this page.')
        return redirect('../accounts/login/')


# Edit contacts view
def edit_contact(request, entry_id):
    if request.user.is_authenticated:
        entry = get_object_or_404(Contact, id=entry_id)

        if request.method == 'POST':
            form = ContactForm(request.POST, instance=entry)
            if form.is_valid():
                form.save()
                messages.success(
                    request, 'Your list has been successfully updated.'
                    )
                return redirect('contact')
        else:
            form = ContactForm(instance=entry)

        return render(
            request, 'edit_contact.html', {'form': form, 'entry': entry}
            )
    else:
        messages.error(request, 'You have to be logged in to show this page.')
        next_url = reverse('edit_contact', args=[entry_id])
        login_url = '/accounts/login' + f'?next={next_url}'
        return HttpResponseRedirect(login_url)


# Delete contact view
def delete_contact(request, entry_id):
    if request.user.is_authenticated:
        entry = get_object_or_404(Contact, id=entry_id)

        if request.method == 'POST':
            entry.delete()
            messages.success(
                request, 'Your entry has been successfully deleted.'
                )
            return redirect('contact')

        return render(request, 'delete_contact.html', {'entry': entry})
    else:
        messages.error(request, 'You have to be logged in to show this page.')
        next_url = reverse('delete_contact', args=[entry_id])
        login_url = '/accounts/login' + f'?next={next_url}'
        return HttpResponseRedirect(login_url)


# Delete account view
def delete_account(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            password = request.POST.get('password')
            if request.user.check_password(password):
                request.user.delete()
                logout(request)
                messages.success(
                    request, 'Your account has been successfully deleted.'
                    )
                return redirect('home')
            else:
                messages.error(
                    request,
                    'Password is invalid. Your account has not been deleted.'
                    )

        return render(request, 'delete_account.html')
    else:
        messages.error(request, 'You have to be logged in to show this page.')
        return redirect('../accounts/login/')


# Public profile view
def public_profile(request, public_link):
    user_profile = get_object_or_404(UserProfile, public_link=public_link)
    medication_entries = MediDisList.objects.filter(user_profile=user_profile)
    doctor_entries = Doctor.objects.filter(user_profile=user_profile)
    contact_entries = Contact.objects.filter(user_profile=user_profile)

    return render(
        request, 'public_profile.html', {
            'user_profile': user_profile,
            'medication_entries': medication_entries,
            'contact_entries': contact_entries,
            'doctor_entries': doctor_entries
            })


# 404 view
def custom_404(request, exception):
    return render(request, '404.html', status=404)
