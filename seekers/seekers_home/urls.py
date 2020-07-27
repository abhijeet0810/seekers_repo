from django.urls import path
from .views import RoomListView, RoomDetailView, RoomCreateView, RoomUpdateView, RoomDeleteView
from . import views

urlpatterns = [
    path('', views.seekers_home, name='seekers-home'),
    path('about/', views.about, name='seekers-home-about'),
    path('rooms/', RoomListView.as_view(), name='seekers-home-rooms'),
    path('rooms/<int:pk>/', RoomDetailView.as_view(), name='seekers-home-rooms-detail'),
    path('rooms/new/', RoomCreateView.as_view(), name='seekers-home-rooms-create'),
    path('rooms/<int:pk>/update', RoomUpdateView.as_view(), name='seekers-home-rooms-update'),
    path('rooms/<int:pk>/delete', RoomDeleteView.as_view(), name='seekers-home-rooms-delete'),
    path('room_seeker/', views.room_seeker, name='seekers-home-room-seeker'),
]
