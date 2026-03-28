# forms.py

from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['guest_name', 'email', 'check_in_date', 'check_out_date']
        widgets = {
            'check_in_date': forms.DateInput(attrs={'type': 'date'}),
            'check_out_date': forms.DateInput(attrs={'type': 'date'}),
        }



from .models import Payment

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['user_name', 'amount', 'payment_method']
        widgets = {
            'payment_method': forms.Select(choices=[('Credit Card', 'Credit Card'), ('PayPal', 'PayPal'), ('Bank Transfer', 'Bank Transfer')]),
        }

from django import forms
from .models import ContactMessage  # Assuming you have a model for contact messages

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage  # Use your ContactMessage model here
        fields = ['name', 'email', 'message']  # Add other fields as needed

        # You can add widgets to customize the form fields
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your Message'}),
        }



#event booking
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['user_name', 'number_of_persons']
