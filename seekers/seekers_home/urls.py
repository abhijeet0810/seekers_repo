from django.urls import path
from .views import (RoomListView,
                    RoomDetailView, 
                    RoomCreateView, 
                    RoomUpdateView, 
                    RoomDeleteView, 
                    RoomSeekerListView, 
                    RoomSeekerDetailView, 
                    RoomSeekerCreateView,
                    RoomSeekerUpdateView,
                    RoomSeekerDeleteView)
from . import views

urlpatterns = [
    path('', views.seekers_home, name='seekers-home'),
    path('about/', views.about, name='seekers-home-about'),
    path('rooms/', RoomListView.as_view(), name='seekers-home-rooms'),
    path('rooms/<int:pk>/', RoomDetailView.as_view(), name='seekers-home-rooms-detail'),
    path('rooms/new/', RoomCreateView.as_view(), name='seekers-home-rooms-create'), # template: rooms_form.html
    path('rooms/<int:pk>/update', RoomUpdateView.as_view(), name='seekers-home-rooms-update'),
    path('rooms/<int:pk>/delete', RoomDeleteView.as_view(), name='seekers-home-rooms-delete'),
    path('room_seeker/', RoomSeekerListView.as_view(), name='seekers-home-room-seeker'),
    path('room_seeker/<int:pk>/', RoomSeekerDetailView.as_view(), name='seekers-home-room-seeker-detail'),
    path('room_seeker/new/', RoomSeekerCreateView.as_view(), name='seekers-home-room-seeker-create'), # template: room_seeker_form.html 
    path('room_seeker/<int:pk>/update', RoomSeekerUpdateView.as_view(), name='seekers-home-room-seeker-update'),
    path('room_seeker/<int:pk>/delete', RoomSeekerDeleteView.as_view(), name='seekers-home-room-seeker-delete'),

]
