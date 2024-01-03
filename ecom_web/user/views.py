from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

def signUpForm(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login-page')

    else:
        form = UserRegistrationForm()
    return render(request, 'user/signup.html', {'form': form})

    