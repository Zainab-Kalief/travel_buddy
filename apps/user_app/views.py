from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import User

def index(request):
    return render(request, 'user_app/index.html')

def sign_up(request):
    entry = User.objects.create_user(request.POST)
    if not type(entry) is dict:
        request.session['user_id'] = entry.id
        return redirect('trip:home')
    else:
        if 'name' in entry:
            messages.add_message(request, messages.INFO, entry['name'], extra_tags='sign_up')
        if 'username_exist' in entry:
            messages.add_message(request, messages.INFO, entry['username_exist'], extra_tags='sign_up')
        if 'password' in entry:
            messages.add_message(request, messages.INFO, entry['password'], extra_tags='sign_up')
        if 'confirm_password' in entry:
            messages.add_message(request, messages.INFO, entry['confirm_password'], extra_tags='sign_up')
        return redirect('user:index')

def log_in(request):
    entry = User.objects.validate_user(request.POST)
    if not type(entry) is dict:
        request.session['user_id'] = entry.id
        return redirect('trip:home')
    else:
        if 'username' in entry:
            messages.add_message(request, messages.INFO, entry['username'], extra_tags='log_in')
        if 'password' in entry:
            messages.add_message(request, messages.INFO, entry['password'], extra_tags='log_in')
        return redirect('user:index')
