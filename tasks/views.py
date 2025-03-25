from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Save the user
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()


            messages.success(request, 'Registration successful!')
            return redirect('tasks:login')  # Redirect to login page (make sure to create a login view later)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RegistrationForm()

    return render(request, 'tasks/register.html', {'form': form})
from django.shortcuts import render

def login(request):
    return render(request, 'tasks/login.html')

# Create your views here.
