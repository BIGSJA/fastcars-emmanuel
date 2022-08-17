from unicodedata import name
from django.urls import path
from .views import cancel_booking_view, confirm_booking_view, dashboard_view, brand_view, registered_users_view, update_brand_view, delete_brand_view, vehicles_view, update_vehicle_details_view, delete_vehicle_view, website_view, update_service_view, delete_service_view, update_contact_view, bookings_view, queries_view, queries_details_view, delete_queries_view, subscribers_view, delete_subscribers_view
urlpatterns = [
    # ==================== ADMIN DASHBOARD PAGE URL ==================
    path('dashboard/', dashboard_view, name='dashboard'),
    # ==================== BRAND PAGE URL ==================
    path('brands/', brand_view, name='brands'),
    # ==================== UPDATE BRAND PAGE URL ==================
    path('update_brand/<int:id>/', update_brand_view, name='update_brand' ),
    # ==================== DELETE BRAND PAGE URL ==================
    path('delete_brand/<int:id>/', delete_brand_view, name='delete_brand'),
    # ==================== VEHICLES PAGE URL ==================
    path('vehicles/', vehicles_view, name='vehicles'),
    # ==================== UPDATE VEHICLE PAGE URL ==================
    path('update_vehicle/<int:id>/', update_vehicle_details_view, name='update_vehicle'),
    # ==================== DELETE VEHICLE PAGE URL ==================
    path('delete_vehicle/<int:id>/', delete_vehicle_view, name='delete_vehicle'),
    # ==================== WEBSITE PAGE URL ==================
    path('website/', website_view, name='website'),
    # ==================== UPDATE SERVICE PAGE URL ==================
    path('update_service/<int:id>/', update_service_view, name='update_service'),
    # ==================== DELETE SERVICE PAGE URL ==================
    path('delete_service/<int:id>', delete_service_view, name='delete_service' ),
    # ==================== UPDATE CONTACT PAGE URL ==================
    path('update_contact/<int:id>/', update_contact_view, name='update_contact'),
    # ==================== BOOKINGS PAGE URL ==================
    path('bookings/', bookings_view, name='bookings'),
    # ==================== CONFIRM BOOKING PAGE URL ==================
    path('confirm_booking/<int:id>/', confirm_booking_view , name='confirm_booking'),
    # ==================== CANCEL BOOKING PAGE URL ==================
    path('cancel_booking/<int:id>/', cancel_booking_view, name='cancel_booking'),
    # ==================== REGISTERED USERS PAGE URL ==================
    path('users/', registered_users_view, name='users'),
    # ==================== QUERIES PAGE URL ==================
    path('queries/', queries_view , name='queries'),
    # ==================== QUERIES DETAILS PAGE URL ==================
    path('queries_details/<int:id>/', queries_details_view , name='queries_details'),
    # ==================== DELETE QUERIES PAGE URL ==================
    path('delete_queries/<int:id>/', delete_queries_view, name='delete_queries'),
    # ==================== SUBSCRIBERS PAGE URL ==================
    path('subscribers/', subscribers_view, name='subscribers'),
    # ==================== DELETE SUBSCRIBERS PAGE URL ==================
    path('delete_subscribers/<int:id>/', delete_subscribers_view, name='delete_subscribers'),
]