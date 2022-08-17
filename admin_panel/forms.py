from typing import Any
from django import forms
from .models import Brand, Vehicle, Booking, Service, Contact

# ================== BRAND UPDATE FORM ================
class BrandUpdateForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ('brand_name',)

# ================== VEHICLE FORM ===============
class VehicleForm(forms.ModelForm):    
    image1 = forms.ImageField(widget=forms.FileInput(attrs={"class": "col-12 form-control mb-3"}))
    image2 = forms.ImageField(widget=forms.FileInput(attrs={"class": "col-12 form-control mb-3"}))
    image3 = forms.ImageField(widget=forms.FileInput(attrs={"class": "col-12 form-control mb-3"}))
    brand = forms.Select(attrs={"class": "col-12 form-select mb-3"})
    vehicle_model = forms.CharField(widget=forms.TextInput(attrs={"class": "col-12 form-control mb-3"}))
    year = forms.CharField(widget=forms.TextInput(attrs={"class": "col-12 form-control mb-3"}))
    mileage= forms.DecimalField(widget=forms.TextInput(attrs={"class": "col-12 form-control mb-3"}))
    chasis_number = forms.CharField(widget=forms.TextInput(attrs={"class": "col-12 form-control mb-3"})) 
    horsepower = forms.IntegerField(widget=forms.TextInput(attrs={"class": "col-12 form-control mb-3"}))
    transmission = forms.Select(attrs={"class": "col-12 form-select mb-3"})
    doors = forms.IntegerField(widget=forms.TextInput(attrs={"class": "col-12 form-control mb-3"}))
    wheel = forms.Select(attrs={"class": "col-12 form-select mb-3"})
    seat = forms.IntegerField(widget=forms.TextInput(attrs={"class": "col-12 form-control mb-3"}))
    color = forms.CharField(widget=forms.TextInput(attrs={"class": "col-12 form-control mb-3"}))
    price = forms.IntegerField(widget=forms.TextInput(attrs={"class": "col-12 form-control mb-3"}))

    class Meta:
        model = Vehicle
        fields = ('image1', 'image2', 'image3', 'brand', 'vehicle_model', 'year', 'mileage', 'chasis_number', 'horsepower', 'transmission', 'doors', 'wheel', 'seat', 'color', 'price')

        def __init__(self, *args: Any, **kwargs: Any) -> None:
            super(VehicleForm, self).__init__(*args, **kwargs)

            for fieldname in ('image1', 'image2', 'image3', 'brand', 'vehicle_model', 'year', 'mileage', 'chasis_number', 'horsepower', 'transmission', 'doors', 'wheel', 'seat', 'color', 'price'):
                self.fields[fieldname].help_text = None

# ============== VEHICLE UPDATE FORM ===================
class VehicleUpdateForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ('image1','image2', 'image3', 'brand', 'vehicle_model', 'year', 'mileage', 'chasis_number', 'horsepower', 'transmission', 'doors', 'wheel', 'seat', 'color', 'price')

# ============== BOOKING FORM =======================
class BookingForm(forms.ModelForm):
    vehicle =  forms.Select(attrs={"class": "col-12 form-select mb-2"})
    pick_up_location = forms.CharField(widget=forms.TextInput(attrs={"class": "col-12 form-control mb-2"}))
    pick_up_date = forms.DateTimeField(widget=forms.TextInput(attrs={"class": "col-12 form-control mb-2", "type":"datetime-local"}))
    drop_off_location = forms.CharField(widget=forms.TextInput(attrs={"class": "col-12 form-control mb-2"}))
    drop_off_date = forms.DateTimeField(widget=forms.TextInput(attrs={"class": "col-12 form-control mb-2", "type":"datetime-local"}))
    class Meta:
        model = Booking
        fields = ('vehicle','pick_up_location', 'pick_up_date', 'drop_off_location', 'drop_off_date',)

# ================= SERVICE UPDATE FORM ================
class ServiceUpdateForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('image','title', 'content',)

# ================= CONTACT UPDATE FORM =================
class ContactUpdateForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('address', 'phone', 'email',)        