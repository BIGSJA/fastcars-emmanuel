from django.shortcuts import render, redirect
from admin_panel.models import Vehicle
from .models import Testimonial, Subscription
from .forms import TestimonialForm
from admin_panel.forms import BookingForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from admin_panel.models import Booking
from fastcars.forms import TestimonialForm
# Create your views here.
# ================= HOME VIEW =============
def home_view(request):
    # Gets all the vehicles and testimonials in the database
    vehicles = Vehicle.objects.all()    
    testimonials = Testimonial.objects.all() 
    # Passes the vehicles, testimonials and booking form into the page
    context={
        'vehicles':vehicles,
        'testimonials':testimonials,
        "booking_form": BookingForm()
    }
    return render(request, 'fastcars/home.html', context)

# ================ VEHICLE DETAILS VIEW ================
def vehicle_details_view(request, id):
    vehicle = Vehicle.objects.get(id=id)
    if request.method == "POST":
        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimony = form.save(commit=False)
            testimony.author = request.user
            testimony.vehicle = vehicle
            testimony.save()
            return redirect('vehicle_details', id=id)
    else:
        form = TestimonialForm() 
    context = {
        'vehicle':vehicle,
        'form':form
    }
    return render(request, 'fastcars/vehicle_details.html', context)

# ================= BOOKINGS VIEW ====================
@login_required
def booking_view(request):
    bookings = Booking.objects.all()
    if request.method == 'POST':
        bookingform = BookingForm(request.POST, request.FILES)
        if bookingform.is_valid():
            booking = bookingform.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, f"You Have Successfully Booked A Vehicle")
            return redirect('home')
    else:
        bookingform = BookingForm()
        messages.error(request, f"Please Try Again")
    context = {
        'bookings':bookings
    }
    return render(request, 'admin_panel/bookings.html', context)

# ================= SUBSCRIPTION VIEW ====================
def subscription_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        if email:
            Subscription(email=email).save()
            messages.success(request, "Your Form Has Been Sent Successfully")
            return redirect('home')
    else:
        messages.error(request, f"Please Try Again")
        return redirect('home')        
