from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from ..user_app.models import User
from .models import Trip, Travel
import datetime

# Create your views here.
def home(request):
    if 'user_id' in request.session:
        user = User.objects.get(id=request.session['user_id'])
        context = {'user': user, 'user_travels': Travel.objects.filter(user=user),
            'travels': Travel.objects.exclude(id__in=user.travel_users.all()).order_by('user__name')}
        return render(request, 'trip_app/home.html', context)
    else:
        return redirect('user:index')

def log_out(request):
    request.session.flush()
    return redirect('user:index')

def add_page(request):
    if 'user_id' in request.session:
        user = User.objects.get(id=request.session['user_id'])
        context = {'user': user}
        return render(request, 'trip_app/add.html', context)
    else:
        return redirect('user:index')

def add_trip(request):
    user = User.objects.get(id=request.session['user_id'])
    entry = Travel.objects.create_travel(request.POST, user)
    if not type(entry) is dict:
        return redirect('trip:home')
    else:
        if 'field' in entry:
            messages.add_message(request, messages.INFO, entry['field'], extra_tags='add')
        if 'from_date' in entry:
            messages.add_message(request, messages.INFO, entry['from_date'], extra_tags='add')
        if 'to_date' in entry:
            messages.add_message(request, messages.INFO, entry['to_date'], extra_tags='add')
        return redirect('trip:add_page')

def join_trip(request, trip_id):
    user = User.objects.get(id=request.session['user_id'])
    entry = Travel.objects.add_user(trip_id, user)
    return redirect('trip:home')

def view_trip(request, trip_id):
    if 'user_id' in request.session:
        trip = Trip.objects.get(id=trip_id)
        context = {'trip': trip, 'planner': trip.travel_trips.all()[0]}
        return render(request, 'trip_app/destination.html', context)
    else:
        return redirect('user:index')
