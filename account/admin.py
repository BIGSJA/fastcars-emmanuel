from django.contrib import admin
from .models import Profile
# Register your models here.

# ================== PROFILE ADMIN =================
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass