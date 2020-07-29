from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin # To tell django, only give permissions to post, create, del a room detail when logedin
from .models import Rooms
from .models import Room_seeker
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.

def seekers_home(request):
    context = {
        'rooms': Rooms.objects.all()
    }
    return render(request, 'seekers_home/seekers_home.html')

def about(request):
    return render(request, 'seekers_home/about.html', {'title': 'About'})

# First we created the function based view (rooms and room_seeker) which lists all the objects 
# from Rooms and Room_seeker model, and display the list of rooms and room seekers
def rooms(request):
    context = {
        'rooms': Rooms.objects.all()
    }
    return render(request, 'seekers_home/rooms.html', context)

# Now, we are creating class based view (RoomListView) which would do the same thing but,
# the reason behind doing this is, we want to further create DetailView, DeleteView and all


class RoomListView(ListView):
    model = Rooms
    template_name = 'seekers_home/rooms.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'rooms'
    ordering = ['-posted_on']

class RoomDetailView(DetailView):
    model = Rooms
    

class RoomCreateView(LoginRequiredMixin, CreateView):
    model = Rooms
    fields = ['title', 'rent','security_deposit', 'size_of_full_apartment', 'duration', 'available_from', 'description']

    # In order to give permission only to the owner to post a new Room lisitng 
    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)

class RoomUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Rooms
    fields = ['title', 'rent','security_deposit', 'size_of_full_apartment', 'duration', 'available_from', 'description']

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        rooms = self.get_object()
        if self.request.user == rooms.posted_by:
            return True
        return False

class RoomDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Rooms
    success_url = '/' # on deletion of post it should direct to the rooms/

    def test_func(self):
        rooms = self.get_object()
        if self.request.user == rooms.posted_by:
            return True
        return False

###############

def room_seeker(request):
    context = {
        'room_seeker': Room_seeker.objects.all()
    }
    return render(request, 'seekers_home/room_seeker.html', context)

class RoomSeekerListView(ListView):
    model = Room_seeker
    template_name = 'seekers_home/room_seeker.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'room_seeker'
    ordering = ['-date_posted']


class RoomSeekerDetailView(DetailView):
    model = Room_seeker


class RoomSeekerCreateView(LoginRequiredMixin, CreateView):
    model = Room_seeker
    fields = ['place', 'profession','budget', 'description']

    # In order to give permission only to the owner 
    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)


class RoomSeekerUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Room_seeker
    fields = ['place', 'profession','budget', 'description']

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        room_seeker = self.get_object()
        if self.request.user == room_seeker.posted_by:
            return True
        return False

class RoomSeekerDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Room_seeker
    success_url = '/' # on deletion of post it should direct to the room_seeker/

    def test_func(self):
        room_seeker = self.get_object()
        if self.request.user == room_seeker.posted_by:
            return True
        return False



    