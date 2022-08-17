from django.urls import path
from .views import about_view, cars_view, contact_view, services_view
urlpatterns = [
    # ==================== ABOUT PAGE URL ==================
    path('about/', about_view, name='about'),
    # ==================== CARS PAGE URL ==================
    path('cars/', cars_view, name='cars'),
    # ==================== CONTACT PAGE URL ==================
    path('contact/', contact_view, name='contact'),
    # ==================== SERVICE PAGE URL ==================
    path('services/', services_view, name='services')
]