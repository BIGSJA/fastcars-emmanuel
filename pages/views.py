from django.shortcuts import render
from admin_panel.models import Vehicle, Service, Contact
from django.core.paginator import Paginator
from .models import Queries
from django.contrib import messages
# Create your views here.

# ====================== ABOUT VIEW ==================
def about_view(request):
    context = {}
    return render(request, 'pages/about.html', context)

# ===================== CARS VIEW =====================
def cars_view(request):
    # Gets all the vehicle in the database
    vehicles = Vehicle.objects.all()
    p = Paginator(vehicles, 3)
    page = request.GET.get('page')
    page_obj = p.get_page(page)
    # Passes page_obj into the page
    context = {
        'page_obj':page_obj
    }
    return render(request, 'pages/cars.html', context)  

# ===================== CONTACT VIEW ==================
def contact_view(request):
    # Gets all the contacts details in the database
    contacts = Contact.objects.all()
    # Checks if the form method is a form method
    if request.method == "POST":
        # Gets form data
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        if name:
            # create and save the queries with a success message
            Queries(name=name, email=email, subject=subject, message=message).save()
            messages.success(request, "Your Form Has Been Sent Successfully")
    else:
        # render the query form with an error message
        messages.error(request, "Please Try Again") 
    # Passes the contacts details into the page           
    context = {
        'contacts':contacts,
    }
    return render(request, 'pages/contact.html', context)

# ===================== SERVICE VIEW ==================
def services_view(request):
    # Gets all the  service details in the database
    services = Service.objects.all()
    # Passes the service details into the page
    context = {
        'services':services
    }
    return render(request, 'pages/services.html', context)        