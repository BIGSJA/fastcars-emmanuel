from django.shortcuts import render, redirect
from admin_panel.models import Booking, Vehicle
from django.contrib.auth.decorators import login_required
from fastcars.models import Testimonial
from fastcars.forms import TestimonialForm
from django.contrib import messages
from django.core.paginator import Paginator
from admin_panel.forms import BookingForm
from .forms import UserUpdateForm, ProfileUpdateForm
# Create your views here.

# ==================== USERS DASHBOARD VIEW ===============
# @login_required makes sure the user is logged in before accessing the page
@login_required
def dashboard_view(request):
    # Passes the booking form into the page
    context = {
    "booking_form": BookingForm()
    }
    return render(request, 'users/users_dashboard.html', context)

# =================== BOOKINGS VIEW ==================
# @login_required makes sure the user is logged in before accessing the page
@login_required
def bookings_view(request):
    # Gets all bookings of current user
    bookings = Booking.objects.filter(user=request.user)
    # Passes the bookings into the page
    context = {
        'bookings':bookings
    }
    return render(request, 'users/users_bookings.html', context)

# =================== TESTIMONIALS VIEW =================
# @login_required makes sure the user is logged in before accessing the page
@login_required
def testimonials_view(request):
    # Gets all testimonials of current user
    testimonials = Testimonial.objects.filter(author=request.user)
    # Checks if the form method is a POST method
    if request.method == "POST":
        # Displays the testimonial form
        form = TestimonialForm(request.POST)
        # checks if form is valid
        if form.is_valid():
            # redirects to users testimonials page with a success message
            form.save()
            messages.success(request, f"Your Testimonial Has Been Posted Succesfully")
            return redirect('users_testimonials')    
    else:
        # if the form is not valid, render the testimonial form with an error message
        form = TestimonialForm() 
        messages.error(request, f"Please Try Again")
    # Passes the testimonials and the testimonial form into the page
    context = {
        'testimonials':testimonials,
        'form':'form'
    }
    return render(request, 'users/users_testimonials.html', context)  

def cars_view(request):
    # Gets all the vehicles in the database
    vehicles = Vehicle.objects.all()

    p = Paginator(vehicles, 3)
    page = request.GET.get('page')
    page_obj = p.get_page(page)
    # Passes the page obj into the page
    context = {
        'page_obj':page_obj
    }
    return render(request, 'users/cars.html', context)

# ====================== EDIT PROFILE VIEW =======================
def edit_profile_view(request):
    # Checks if the form method is a POST method
    if request.method == "POST":
        # Displays the user form & profile form with the details already in it
        user_form = UserUpdateForm(request.POST or None, instance = request.user)
        profile_form = ProfileUpdateForm(request.POST or None, request.FILES or None, instance = request.user.profiles)
        # Checks if the form is valid
        if user_form.is_valid() and profile_form.is_valid():
            # Save the form data
            user_form.save()
            profile_form.save()
            # Return success message & redirect to home page
            messages.success(request, 'Account Profile Updated Successfully')
            return redirect('users_dashboard')
    else:
        # Displays the user form & profile form with the details already in it without a POST
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profiles) 
        messages.error(request, 'Please Try Again')
    # Renders edit profile page with user & profile form
    context = {
        'user_form':user_form,
        'profile_form':profile_form
    }
    return render(request, 'users/edit_profile.html', context)    