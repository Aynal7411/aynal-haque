from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import BusinessRegistrationForm

def register_business(request):
    if request.method == 'POST':
        form = BusinessRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = form.cleaned_data['password']  # In real apps, use set_password()
            user.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('dashboard')  # Redirect to dashboard or success page
    else:
        form = BusinessRegistrationForm()
    return render(request, 'register2.html', {'form': form})




@login_required
def dashboard(request):
    return render(request, 'dashboard.html')




