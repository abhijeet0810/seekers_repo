from django.shortcuts import render
from django.http import HttpResponse
from .models import Rooms
from .models import Room_seeker

# Create your views here.

def seekers_home(request):
    context = {
        'rooms': Rooms.objects.all()
    }
    return render(request, 'seekers_home/seekers_home.html')

def about(request):
    return render(request, 'seekers_home/about.html', {'title': 'About'})

def rooms(request):
    context = {
        'rooms': Rooms.objects.all()
    }
    return render(request, 'seekers_home/rooms.html', context)

def room_seeker(request):
    context = {
        'room_seeker': Room_seeker.objects.all()
    }
    return render(request, 'seekers_home/room_seeker.html', context)

    