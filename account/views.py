from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

# ===================== REGISTRATION VIEW ===================
def registration_view(request):
    # Checks if the form method is a POST method
    if request.method == 'POST':
        # Get form data
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        repeat_password = request.POST['repeat_password']

        # Checks if the password & repeat password matches
        if password == repeat_password:
            # Checks if the username exists in the database
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username Taken')
                return redirect('registration')
            # Checks if the email exists in the database    
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email Taken')
                return redirect('registration')
            else:
                # Create new user with a sucess message and redirect user to login page
                User.objects.create_user(
                    username=username, 
                    first_name=firstname,
                    last_name=lastname,
                    email=email, 
                    password=password
                    )
                messages.success(request, 'Account Created Successfully')
                return redirect('login')
        else:
            # If the password & repeat password doesn't match return an error message
            messages.info(request, 'Password does not match')
            return redirect('registration')         
    context = {}
    return render(request, 'account/registration.html', context)


# ====================== LOGIN VIEW ==========================
def login_view(request):
    # Checks if the form method is a POST method
    if request.method == 'POST':
        # Get form data
        email = request.POST['email']
        password = request.POST['password']
        # Checks if the user's email exists in the database
        if User.objects.all().filter(email=email).exists():
            # Get username of user based on user's email from database
            username = User.objects.get(email=email).username
            # Authenticate user
            user = authenticate(username=username, password=password)
            # Checks if user is a staff
            if user is not None and user.is_staff:
                # Login user & redirect to is_staff dashboard
                auth.login(request,user)
                return redirect('dashboard')
            # Checks if user is not a staff
            elif user is not None and not user.is_staff:
                # login user & redirect to home page
                auth.login(request,user)
                return redirect('users_dashboard')
            # if user is not authenticated, return error message    
            else:
                # returned error message
                messages.error(request, f"Incorrect email or password")
                # renders login page to the user
                return redirect('login') 
        # if user's email does not exist in the database, return an error message               
        else:
            # returned error message
            messages.error(request, f"Please enter a valid email")
            # renders the login page to the user
            return redirect('login')
    context = {}
    return render(request, 'account/login.html', context)

