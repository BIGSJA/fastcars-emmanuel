from django.contrib import admin
from .models import Testimonial, Subscription
# Register your models here.

# ================= TESTIMONIAL ADMIN ======================
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    pass

# ================= SUBSCRIPTION ADMIN ====================
@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    pass