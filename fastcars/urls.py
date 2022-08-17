from django.urls import path
from .views import home_view, vehicle_details_view, booking_view, subscription_view

urlpatterns = [
    # ==================== HOME PAGE URL ==================
    path('', home_view, name='home'),
    # ==================== VEHICLE DETAILS PAGE URL ==================
    path('vehicle_details/<int:id>/', vehicle_details_view, name='vehicle_details'),
    # ==================== BOOKINGS PAGE URL ==================
    path('booking/', booking_view, name='booking'),
    # ==================== SUBSCRIPTION URL ==================
    path('subscription/', subscription_view, name='subscription')
]