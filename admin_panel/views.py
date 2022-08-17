from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking, Brand, Vehicle, Service, Contact
from pages.models import Queries
from fastcars.models import Subscription
from django.contrib import messages
from .forms import BrandUpdateForm, VehicleForm, VehicleUpdateForm, ServiceUpdateForm, ContactUpdateForm
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

# ======================== DASHBOARD VIEW ========================
# @login_required makes sure the user is logged in before accessing the page
@login_required
def dashboard_view(request):
    # It's Get all the bookings in the database
    booking_count = Booking.objects.all().count()
    # It's Get all the queries in the database
    queries_count = Queries.objects.all().count()
    # It's Get all the registered users in the database
    registered_users = User.objects.all().count()
    # it's Get all the total vehicles in the database
    total_vehicle = Vehicle.objects.all().count()
    # it's Get all the subscribers in the database
    subscribers = Subscription.objects.all().count()

    # The context passes all the data into the dashboard page
    context = {
        "booking_count": booking_count,
        "queries_count": queries_count,
        "registered_users": registered_users,
        "total_vehicle":total_vehicle,
        "subscribers":subscribers
    }
    return render(request, 'admin_panel/dashboard.html', context)

# ======================== BRAND VIEW ==========================
# @login_required makes sure the user is logged in before accessing the page
@login_required
def brand_view(request):
    # Get all the vehicle brands in the database
    brand = Brand.objects.all()
    # Checks if the form method is a POST method 
    if request.method == 'POST':
        # Gets the name of the new brand entered 
        name = request.POST['name']
        # if a name is being entered, the following functions should be executed
        if name:
            # Create an instance of the brand with the new brand name and save the new brand name in the database
            Brand(brand_name=name).save()
            # redirect to the brands page with a success message
            messages.success(request, "You have successfully added a brand")
            # return redirect('brands')
    else:
        # if no brand is entered, return to the brands page with an error message
        messages.error(request, "Please Try Again")
        # return redirect('brands')
    # Passes the brand into the page    
    context = {
        'brand': brand,
    }
    return render(request, 'admin_panel/brands.html', context)

# ========================= EDIT BRAND VIEW =======================
# @login_required makes sure the user is logged in before accessing the page
@login_required
# Get the id of the brand
def update_brand_view(request, id):
    # Get the brand with the id
    brand = Brand.objects.get(id=id)
    # Checks if the form method is a POST method 
    if request.method == "POST":
        # Displays the form with a brand name info already in it
        form = BrandUpdateForm(request.POST or None , instance=brand)
        # Checks if the form is valid
        if form.is_valid():
            # redirects the admin to brand page with a success message
            form.save()
            messages.success(request, "You have Successfully Updated Your Brand")
            # return redirect('brands')
    else:
        # if the form is not valid, render the  brand update form page with an error message
         form = BrandUpdateForm(instance=brand)
         messages.error(request, "Please Try Again")
    # Passes the form and the single brand into the page        
    context={
        'form':form,
        'brand':brand
    }
    return render(request, 'admin_panel/update_brand.html', context)

# ======================== DELETE BRAND VIEW =====================
# @login_required makes sure the user is logged in before accessing the page
@login_required
# Get the id of the brand
def delete_brand_view(request,id):
    # Get the vehicle with the id
    brand = get_object_or_404(Brand, id=id)
    # delete the vehicle
    brand.delete()
    # redirect the admin to the brands page with a succes message
    messages.success(request, "You have Successfully Deleted Your Post ")
    return redirect('vehicles')

# ========================= VEHICLES VIEW ============================
# @login_required makes sure the user is logged in before accessing the page
def vehicles_view(request):
    # Get all the vehicles in the database
    vehicles = Vehicle.objects.all()
    # Paginates the vehicles in the page
    p = Paginator(vehicles, 3)
    page = request.GET.get('page')
    page_obj = p.get_page(page)
    # Checks if the form method is a POST method
    if request.method == "POST":
        # if form is a POST method, pull out vehicle form
        vehicleform = VehicleForm(request.POST, request.FILES)
        # Checks if the admin meets the requirements of the vehicle form
        if vehicleform.is_valid():
            # If the requirements is been met, redirect the admin to vehicles page with a success message
            vehicleform.save()
            messages.success(request, f"You Have Successfully Added A Vehicle")
            return redirect('vehicles')
    else:
        # if the requirements is not been met, the vehicle form should re-appear with an error message
        vehicleform = VehicleForm()
        messages.error(request, f"Please Try Again")

    # Passes the paginated vehicles & vehicle form into the page    
    context = {
        'page_obj':page_obj,
        'vehicleform':vehicleform
    }
    return render(request, 'admin_panel/vehicles.html', context)

# ======================== VEHICLE UPDATE VIEW ==================
# @login_required makes sure the user is logged in before accessing the page
@login_required
# Get the id of the vehicle
def update_vehicle_details_view(request, id):
    # Get the vehicle with the id
    vehicle = Vehicle.objects.get(id=id)
    # Checks if the form method is a POST method
    if request.method == "POST":
        # Dsiplays the form with a vehicle info already in it
        form = VehicleUpdateForm(request.POST or None , request.FILES, instance=vehicle)
        # Checks if form is valid
        if form.is_valid():
            # redirects the admin to vehicles page with a success message
            form.save()
            messages.success(request, "You have Successfully Updated Your Vehicle")
            return redirect('vehicles')
    else:
        # if the form is not valid, render the edit vehicle page with an error message
         form = VehicleUpdateForm(instance=vehicle)
         messages.error(request, "Please Try Again")
    # Passes the form and the single vehicle into the page     
    context = {
        'form':form,
        'vehicle':vehicle
    }
    return render(request, 'admin_panel/update_vehicle.html', context)

# ====================== DELETE VEHICLE VIEW ===================
# @login_required makes sure the user is logged in before accessing the page
@login_required
# Get the id of the vehicle
def delete_vehicle_view(request, id):
    # Get the vehicle with the id
    vehicle = get_object_or_404(Vehicle, id=id)
    # delete the vehicle
    vehicle.delete()
    # redirect the admin to the vehicles page with a succes message
    messages.success(request, "You have Successfully Deleted Your Post ")
    return redirect('vehicles')

# ===================== WEBSITE VIEW =======================
# @login_required makes sure the user is logged in before accessing the page
@login_required
def website_view(request):
    # Gets all the service details in the database
    services = Service.objects.all()
    # Gets all the contact details in the database
    contacts = Contact.objects.all()
    # Passes the services details & contacts details into the page
    context = {
        'services':services,
        'contacts':contacts
    }
    return render(request, 'admin_panel/website.html', context)

# ===================== UPDATE SERVICE VIEW ==================
# @login_required makes sure the user is logged in before accessing the page
@login_required
# Get the id of the service details
def update_service_view(request, id):
    # Get the service details with the id
    service = Service.objects.get(id=id)
    # Checks if the form method is a POST method
    if request.method == "POST":
        # Displays the form with the service details info already in it
        form = ServiceUpdateForm(request.POST or None , request.FILES, instance=service)
        # Checks if form is valid
        if form.is_valid():
            # redirects to websites page with a success message
            form.save()
            messages.success(request, "You have Successfully Updated Your Service Page")
            return redirect('website')
    else:
        # if the form is not valid, render the update service page with an error message
         form = ServiceUpdateForm(instance=service)
         messages.error(request, "Please Try Again")
    # Passes service details & update form into the page   
    context = {
        'service':service,
        'form':form
    }
    return render(request, 'admin_panel/update_service.html', context)

# ====================== DELETE SERVICE VIEW ===================
# @login_required makes sure the user is logged in before accessing the page
@login_required
# Get the id of the service details
def delete_service_view(request, id):
    # Get the service details with the id
    service = get_object_or_404(Service, id=id)
    # delete service
    service.delete()
    # redirect the admin to the vehicles page with a succes message
    messages.success(request, "You have Successfully Deleted One Of The Service Content")
    return redirect('website')

# ===================== UPDATE CONTACT VIEW ==================
# @login_required makes sure the user is logged in before accessing the page
@login_required
# Get the id of the service details
def update_contact_view(request, id):
    # Get the service details with the id
    contact = Contact.objects.get(id=id)
    # Checks if the form method is a POST method
    if request.method == "POST":
        # Displays the form with the contact details info already in it
        form = ContactUpdateForm(request.POST or None , request.FILES, instance=contact)
        # Checks if form is valid
        if form.is_valid():
            # redirects to websites page with a success message
            form.save()
            messages.success(request, "You have Successfully Updated Your Service Page")
            return redirect('website')
    else:
         # if the form is not valid, render the update service page with an error message
         form = ContactUpdateForm(instance=contact)
         messages.error(request, "Please Try Again")
    # Passes contact details & contact update form into the page     
    context = {
        'contact':contact,
        'form':form
    }
    return render(request, 'admin_panel/update_contact.html', context)

# ==================== BOOKINGS VIEW ==================
# @login_required makes sure the user is logged in before accessing the page
@login_required
def bookings_view(request):
    # Get all the bookings in the database
    bookings = Booking.objects.all()
    # Passes the bookings into the page
    context = {
        'bookings':bookings
    }
    return render(request, 'admin_panel/bookings.html', context)

# ==================== CONFIRM BOOKING VIEW ==================
# @login_required makes sure the user is logged in before accessing the page
@login_required
# Get the id of the booking
def confirm_booking_view(request, id):
    # Get the booking with the id
    booking = Booking.objects.get(id=id)
    # Sets the booking to active
    booking.confirmed = True
    # redirects the admin to bookings page with a success message
    booking.save()
    messages.success(request, "Your Booking Has Been Confirmed")
    return redirect('bookings')

# ==================== CANCEL BOOKING VIEW ==================
# @login_required makes sure the user is logged in before accessing the page
@login_required
# Get the booking based on the id 
def cancel_booking_view(request, id):
    # Get the booking with the id
    booking = get_object_or_404(Booking, id=id)
    # Sets the booking to Inactive
    booking.confirmed = False
    # redirects the admin to bookings page with a success message
    booking.save()
    messages.success(request, f"Your Booking Has Been Cancelled")    
    return redirect('bookings')

# ==================== REGISTERED USERS VIEW ==================
# @login_required makes sure the user is logged in before accessing the page
@login_required       
def registered_users_view(request):
    # Gets all the user in the database
    user = User.objects.all()
    # Passes the user details into the page
    context = {
        'user':user
    }
    return render(request, 'admin_panel/users.html', context)      

# ================= QUERIES VIEW ==================
# @login_required makes sure the user is logged in before accessing the page
@login_required
def queries_view(request):
    # Get all the queries in the database
    queries = Queries.objects.all()
    # Passes the queries into the page
    context = {
        'queries':queries
    }
    return render(request, 'admin_panel/queries.html', context)

# ================= QUERIES DETAILS VIEW ================== 
# @login_required makes sure the user is logged in before accessing the page
@login_required
# Get the queries based on the id 
def queries_details_view(request, id):
    # Get the queries based on the id 
    queries = get_object_or_404(Queries, id=id)
    # Passes the queries into the page
    context = {
        'queries':queries
    }
    return render(request, 'admin_panel/queries_details.html', context)

# ================= DELETE QUERIES VIEW ================== 
# @login_required makes sure the user is logged in before accessing the page
@login_required
# Get the id of the vehicle
def delete_queries_view(request, id):
    # Get the vehicle with the id
    queries = get_object_or_404(Queries, id=id)
    # delete the vehicle
    queries.delete()
    # redirect the admin to the vehicles page with a succes message
    messages.success(request, "You have Successfully Deleted A Query")
    return redirect('queries')

# ======================= SUBSCRIBERS VIEW =================
# @login_required makes sure the user is logged in before accessing the page
@login_required
def subscribers_view(request):
    # Get all the subscription in the database
    subscribers = Subscription.objects.all()
    # Passes the subscribers into the page
    context = {
        'subscribers':subscribers
    }
    return render(request, 'admin_panel/subscribers.html', context)

# ================= DELETE SUBSCRIBERS VIEW ================== 
# @login_required makes sure the user is logged in before accessing the page
@login_required
# Get the id of the subscriber
def delete_subscribers_view(request, id):
    # Get the subscribers with the id
    subscribers = get_object_or_404(Subscription, id=id)
    # delete the vehicle
    subscribers.delete()
    # redirect the admin to the vehicles page with a succes message
    messages.success(request, "You have Successfully Deleted A Query")
    return redirect('subscribers')
