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

import json
import os
from django.shortcuts import render
from django.http import JsonResponse

def dictionary_search(request):
    meaning = None
    error = None

    if request.method == 'POST':
        word = request.POST.get('word', '').strip()

        if word:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            json_path = os.path.join(base_dir, 'BengaliDictionary.json')

            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Search case-insensitive
            results = [
                  entry for entry in data 
    if entry.get('English Word') and entry['English Word'].lower() == word.lower()
]

            if results:
                meaning = results[0]['Bangla Meaning']
            else:
                error = "Word not found."
        else:
            error = "Please enter a word."

    return render(request, 'dictionary_search.html', {'meaning': meaning, 'error': error})


