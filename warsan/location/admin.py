from django.contrib import admin
from .models import Location

# Register your models here.
class LocationAdmin(admin.ModelAdmin):
    list_display = ('state', 'region', 'district', 'vaccination_center')
