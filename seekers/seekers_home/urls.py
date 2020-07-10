from django.urls import path
from . import views

urlpatterns = [
    path('', views.seekers_home, name='seekers-home'),
    path('about/', views.about, name='seekers-home-about'),
    path('rooms/', views.rooms, name='seekers-home-rooms'),
]
