from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Hotel
from .forms import ReservationForm
from .models import Destination




def index(request):
  return render(request, 'index.html')
  
def about(request):
  return render(request, 'about.html')

def service(request):
  return render(request, 'service.html')

def package(request):
  return render(request, 'package.html')

def destination(request):
  return render(request, 'destination.html')

def booking(request):
  return render(request, 'booking.html')

def team(request):
  return render(request, 'team.html')

def testimonial(request):
  return render(request, 'testimonial.html')

def page(request):
  return render(request, '404.html')

def contact(request):
  return render(request, 'contact.html')

#login view

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# User Registration
def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if not User.objects.filter(username=username).exists():
                User.objects.create_user(username=username, email=email, password=password)
                messages.success(request, "User registered successfully!")
                return redirect('user_login')
            else:
                messages.error(request, "Username already exists!")
        else:
            messages.error(request, "Passwords do not match!")
    return render(request, 'register.html')

# User Login


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Log the user in
            if not user.is_staff:  # Only show the message to non-admin users
                messages.success(request, f"Welcome, {user.username}!")
            return redirect('index')  # Redirect to the homepage (or any other page)
        else:
            if not user.is_staff:  # Only show the error message to non-admin users
                messages.error(request, "Invalid credentials!")  # Show an error if credentials are incorrect
    return render(request, 'user_login.html')  # Render the login page


# Logout
def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('index')


# reservation

def hotel_list(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotel_list.html', {'hotels': hotels})

def reserve_hotel(request, hotel_id):
    hotel = Hotel.objects.get(id=hotel_id)
    success = False

    if request.method == 'POST':
        form = ReservationForm(request.POST)

        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.hotel = hotel
            reservation.save()
            success = True
            form = ReservationForm()      # clear form after booking
    else:
        form = ReservationForm()

    return render(request, 'reserve_hotel.html', {'form': form, 'hotel': hotel, 'success': success})

#booking view

def choose_destination(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        number_of_persons = request.POST.get('number_of_persons')
        destination_name = request.POST.get('destination')

        # Store booking details in the session
        request.session['user_name'] = user_name
        request.session['number_of_persons'] = number_of_persons
        request.session['destination'] = destination_name

        return redirect('payment')

    destinations = Destination.objects.all()
    return render(request, 'choose_destination.html', {'destinations': destinations})

#payment


from .models import Payment

from .forms import PaymentForm
from django.urls import reverse

def payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.status = 'Success'  # Assume success for simplicity
            payment.save()
            return redirect('index')  # Redirect to the home page
    else:
        form = PaymentForm()

    return render(request, 'payment.html', {'form': form})



#contact
# travel_app/views.py
from django.shortcuts import render, redirect
from .models import ContactMessage
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        # Get data from the form
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        
        # Save to database
        ContactMessage.objects.create(name=name, email=email, subject=subject, message=message)
        return redirect('index')  # Redirect to the same page after submission

    return render(request, 'contacts.html')


from django.shortcuts import render,get_object_or_404
from .models import Event,Booking
from .forms import BookingForm

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event.html', {'events': events})

def book_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.event = event
            booking.save()
            return redirect('payment')  # Replace 'payment_page' with the actual URL name of your payment page
    else:
        form = BookingForm()

    return render(request, 'book_event.html', {'event': event, 'form': form})

#footer
#Privacy policy

def privacy_policy(request):
    return render(request, 'privacy_policy.html')  # Rendering your template

#cookies

def cookies_policy(request):
    return render(request, 'cookies_policy.html')  # Rendering the cookies template

#Help

def help_page(request):
    return render(request, 'help.html')

#FAQ

def faq_page(request):
    return render(request, 'faq.html')


#terms and condition

def terms_page(request):
    return render(request, 'terms.html')

