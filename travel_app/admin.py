# admin.py
# admin.py

from django.contrib import admin
from .models import Hotel, Reservation

class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'price_per_night', 'image')  # Add image to the list display
    search_fields = ('name', 'location')

admin.site.register(Hotel, HotelAdmin)
admin.site.register(Reservation)

# contact

from django.contrib import admin
from .models import ContactMessage

admin.site.register(ContactMessage)

# event booking
from .models import Event,Booking

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'duration', 'price')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'event', 'number_of_persons', 'booking_date')


from django.contrib import admin
from .models import Payment

# Register the Payment model
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'amount', 'payment_method', 'status')
    search_fields = ('user_name', 'payment_method', 'status')

