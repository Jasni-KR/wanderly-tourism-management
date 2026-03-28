# models.py

from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='hotel_images/', null=True, blank=True)  

    def __str__(self):
        return self.name

class Reservation(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=100)
    email = models.EmailField()
    check_in_date = models.DateField()
    check_out_date = models.DateField()

    def __str__(self):
        return f"Reservation by {self.guest_name} for {self.hotel.name}"
    
#booking



class Destination(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
#payment
class Payment(models.Model):
    user_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"{self.user_name} - {self.payment_method} - {self.status}"

# travel_app/models.py
from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    subject = models.CharField(max_length=255, default='General Inquiry')
    def __str__(self):
        return self.name

#event
class Event(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    capacity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='event_images/')

    def __str__(self):
        return self.name

class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    email = models.EmailField()
    number_of_persons = models.IntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name} - {self.event.name}"
