from distutils.command.upload import upload
from django.db import models
from django.template.defaultfilters import slugify
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
# Create your models here.
# ================= BRAND MODEL ================
class Brand(models.Model):
    brand_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(null=True, unique=True, blank=True)

    def __str__(self):
        return self.brand_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.brand_name)
        return super().save(*args, **kwargs)

# ================ VEHICLE MODEL ================
class Vehicle(models.Model):
    transmission_choices = [
        ('None', 'None'),
        ('Manual','Manual'),
        ('Automatic','Automatic')
    ]

    wheel_choices = [
        ('None', 'None'),
        ('2','2'),
        ('4','4')
    ]

    image1 = models.ImageField(validators=[FileExtensionValidator(
    ['png','jpg','jpeg'])], upload_to='vehicle_images')
    image2 = models.ImageField(validators=[FileExtensionValidator(
    ['png','jpg','jpeg'])], upload_to='vehicle_images')   
    image3 = models.ImageField(validators=[FileExtensionValidator(
    ['png','jpg','jpeg'])],upload_to='vehicle_images')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='vehicles')
    vehicle_model = models.CharField(max_length=200)
    year = models.CharField(max_length=5)
    mileage = models.DecimalField(max_digits=10, decimal_places=4)
    chasis_number = models.CharField(max_length=18)
    horsepower = models.IntegerField()
    transmission = models.CharField(
    max_length=10, choices=transmission_choices, default='None')
    doors = models.IntegerField()
    wheel = models.CharField(max_length=10, choices=wheel_choices, default='None')
    seat = models.IntegerField()
    color = models.CharField(max_length=20)
    price = models.IntegerField()
    slug = models.SlugField(unique=True, null=True, blank=True)


    def comments(self):
        return self.comment_set.all()

    def comments_count(self):
        return self.comment_set.all().count()  
          
    class Meta:
        ordering = ('-brand',)

    def __str__(self):
        return f"{self.brand} {self.vehicle_model}"

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.brand}_{self.vehicle_model}")
        return super().save(*args, **kwargs)

# ================ BOOKING MODEL ================
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="bookings")
    pick_up_location = models.CharField(max_length=500)
    pick_up_date = models.DateTimeField()
    drop_off_location = models.CharField(max_length=500)
    drop_off_date = models.DateTimeField()
    confirmed = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}: {self.vehicle.brand} {self.vehicle.vehicle_model} ~ {self.pick_up_date} - {self.drop_off_date}"

# ================ SERVICE MODEL =================
class Service(models.Model):
    image = models.ImageField(validators=[FileExtensionValidator(
    ['png','jpg','jpeg'])], upload_to='service_icons')
    title = models.CharField(max_length=30)
    content = models.TextField()

    def __str__(self):
        return self.title

# =============== CONTACT MODEL ===================
class Contact(models.Model):
    address = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    email = models.CharField(max_length=30, blank=True)

