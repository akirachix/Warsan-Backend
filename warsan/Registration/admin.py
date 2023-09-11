from django.contrib import admin
from .models import Registrations
# Register your models here.


class RegistrationsAdmin(admin.ModelAdmin):
    list_display = ("email","date_created","date_updated") 

admin.site.register(Registrations, RegistrationsAdmin)