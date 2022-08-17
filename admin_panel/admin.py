from django.contrib import admin
from .models import Brand, Vehicle, Booking, Service, Contact
# Register your models here.

# ===================== BRAND ADMIN ==================
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass

# ===================== VEHICLE ADMIN ==================
@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    pass

# =================== BOOKING ADMIN =====================
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    pass

# ================== SERVICE ADMIN ==================
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass

# ================= CONTACT ADMIN =================
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass