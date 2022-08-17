from django.urls import path
from .views import dashboard_view, bookings_view, testimonials_view, cars_view, edit_profile_view
from django.contrib.auth import views
urlpatterns = [
    path('users_dashboard/', dashboard_view, name='users_dashboard'),
    path('users_bookings/', bookings_view, name='users_bookings'),
    path('users_testimonials/', testimonials_view, name='users_testimonials'),
    path('users_cars/', cars_view, name='users_cars'),
    path('edit_profile', edit_profile_view, name='edit_profile'),
    # ================== LOGOUT PAGE URL ==================
    path('logout/', views.LogoutView.as_view(template_name='account/logout.html'), name='logout')
]