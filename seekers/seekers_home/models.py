from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from django.urls import reverse

# Create your models here.

class Rooms(models.Model):
    RENT = 'RENT'
    SUB_RENT = 'SUB RENT'

    Full_apartment = 'Full apartment'
    Sharing_apartnent = 'Sharing apartnent'
    Room_sharing = 'Room sharing'
    Studio = 'Studio'

    Furnished = 'Furnished'
    Semi_furnished = 'Semi furnished'
    Non_furnished = 'Non furnished'
    
    Anyone = 'Anyone'
    Yes = 'Yes'
    No = 'No'

    Month = 'Month/s'
    Week =  'Week/s'
    Day =  'Day/s'

    Apartment_type = [
        (Furnished, 'Furnished'),
        (Semi_furnished, 'Semi furnished'),
        (Non_furnished,'Non furnished'),
    ]

    AVAILABLE_FOR_CHOICES = (
        ('Male', 'Male'),
        ('Female','Female'),
        ('Anysex','Anysex'),
        ('Single', 'Single'),
        ('Couple','Couple'),
        ('Anyone','Anyone'),
        
    )

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

    yes_no_choices= [
        (Yes, 'Yes'),
        (No, 'No'),
    ]

    duration_choices = [
        ('Month/s', 'Month/s'),
        ('Week/s', 'Week/s'),
        ('Day/s', 'Day/s'),
    ]

    title = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    pin_code = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    available_for = MultiSelectField(choices= AVAILABLE_FOR_CHOICES, default= Anyone)
    nearest_station = models.CharField(max_length=100)
    rent = models.IntegerField()
    security_deposit = models.IntegerField()
    apartment_type = models.CharField(max_length=30, choices=Apartment_type, default=Non_furnished,)
    rent_type = models.CharField(max_length=10, choices=RENT_TYPE_CHOICES, default=RENT,)
    share_type = models.CharField(max_length=100, choices= SHARE_TYPE_CHOICES, default=Full_apartment,)
    size_of_full_apartment = models.IntegerField()
    guarantor_required = models.CharField(max_length=10, choices= yes_no_choices, default=No,)
    contract = models.CharField(max_length=10, choices= yes_no_choices, default=No,)
    apl_caf = models.CharField(max_length=10, choices= yes_no_choices, default=No,)

    available_from = models.DateTimeField()
    duration = models.IntegerField(max_length=3, default=0)
    duration_m_w_d = models.CharField(max_length=10, choices= duration_choices, default= Month)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=1024) # inside this box in gray (Describe more about you apartment such as amenities or other information in the apartment like WIFI/ Parking Space/ Electricity/ Pet Allowed/ Dishwasher/ Balcony.....etc.)
    posted_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    # this will route the path to the detail view after creating the new post
    def get_absolute_url(self):
        return reverse('seekers-home-rooms-detail', kwargs={'pk': self.pk})

 
    # contact_number = models.CharField(max_length=100) # In-app messaging portal
    # contact_mail = models.CharField(max_length=100) # Mail address can not be shared publically
    # 
    # photos_upload = #
    
    


class Room_seeker(models.Model):
    place = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    budget = models.IntegerField()
    description = models.CharField(max_length=1024)
    posted_by = models.OneToOneField(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    # make a boolean attribute  as: is_room_seeker_authenticated (True/False)
    # --- It would be True when the Room seeker is added otherwise False
    # 
    # in base.html -- { if room_seekers.is_room_seeker_authenticated } : You are already Added { else } : Add yourself 
    
    def __str__(self):
        return self.place

    def get_absolute_url(self):
        return reverse('seekers-home-room-seeker-detail', kwargs={'pk': self.pk})
    
    # Make a dependent/chained dropdown list of Region and City
    # gender: from register model
    # DOB : from register model
    # Looking for accomodation from = Month
    # Looking for the duration of = Days/Weeks/Months
    # metro = # (multi choice) from list of Metro stations: M1, M2, M3, M4, M5.......
    # rer =  # (multi choice) from list of RER stations: RER A, RER B, RER c, .....
    # bus_station = models.CharField(max_length=100)
