from django.shortcuts import render, redirect
from django.contrib import messages


def home(request):
    return render(request, 'index.html')

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        messages.error(request, 'You have to be logged in to show this page.')
        return redirect('../accounts/login/')
