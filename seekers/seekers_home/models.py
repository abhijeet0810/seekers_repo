from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Rooms(models.Model):
    RENT = 'RENT'
    SUB_RENT = 'SUB RENT'
    Full_apartment = 'Full apartment'
    Sharing_apartnent = 'Sharing apartnent'
    Room_sharing = 'Room sharing'
    Studio = 'Studio'
    RENT_TYPE_CHOICES = [
        (RENT, 'Rent'),
        (SUB_RENT, 'Sub Rent'),
    ]
    SHARE_TYPE_CHOICES = [
        (Full_apartment,'Full apartment'),
        (Sharing_apartnent, 'Sharing apartnent'),
        (Room_sharing, 'Room sharing'),
        (Studio,'Studio'),
    ]
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    pin_code = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    nearest_station = models.CharField(max_length=100)
    rent = models.IntegerField() # Euro symbol at the end :(
    security_deposit = models.IntegerField() # Euro symbol at the end :(
    rent_type = models.CharField(max_length=10, choices=RENT_TYPE_CHOICES, default=RENT,) # How to mention choices between two here : Rent / Sub-Rent
    share_type = models.CharField(max_length=100, choices= SHARE_TYPE_CHOICES, default=Full_apartment,) # choices: Full apartment / Sharing apartnent / Room sharing / Studio
    size_of_full_apartment = models.IntegerField() # in m**2

    available_from = models.DateTimeField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=1024)

    def __str__(self):
        return self.title

    # apartment_type = # choices: Furnished / Semi-Furnished / Non-Furnished
    # available_for = # : (Multi choice) Single / Couple and Male / Female / Anysex
    # available_from = models.DateTimeField()
    # duration = models.CharField(max_length=100) # make it d/m/y
    # guarantor_required = # : Yes/ No
    # contract = # : Yes/No
    # amenities = # : (Multi choice) WIFI/ Parking Space/ Electricity/ Pet Allowed/ Dishwasher/ Balcony.....etc.
    # contact_number = models.CharField(max_length=100)
    # contact_mail = models.CharField(max_length=100)
    # posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    # date_posted = models.DateTimeField(default=timezone.now)
    # photos_upload = #
    
    


class Room_seeker(models.Model):
    place = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    budget = models.IntegerField()
    description = models.CharField(max_length=1024)
    posted_by = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.place
    
    # gender: from register model
    # DOB : from register model
    # metro = # (multi choice) from list of Metro stations: M1, M2, M3, M4, M5.......
    # rer =  # (multi choice) from list of RER stations: RER A, RER B, RER c, .....
    # bus_station = models.CharField(max_length=100)
