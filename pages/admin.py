from django.contrib import admin
from .models import Queries
# Register your models here.

# ==================== QUERIES ADMIN ==================
@admin.register(Queries)
class QueriesAdmin(admin.ModelAdmin):
    pass