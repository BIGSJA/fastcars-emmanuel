from django.urls import path
from .views import registration_view, login_view
urlpatterns = [
    # ================== REGISTRATION PAGEURL ===============
    path('registration/', registration_view, name='registration'),
    # ================== LOGIN PAGE URL =================
    path('login/', login_view, name='login'),
]