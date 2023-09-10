from django.contrib import admin
from phonenumber_field.formfields import PhoneNumberField
from .models import HealthWorker

class HealthAdmin(admin.ModelAdmin):
    list_display = ("full_name", "phone_number", "location", "hospital")  # Replace the fields with "full_name"
    search_fields = ("first_name","middle_name", "last_name", "location", "hospital")
    list_filter = ("location", "hospital")

    def full_name(self, obj):
        return obj.full_name()  

    full_name.short_description = "Full Name"  

admin.site.register(HealthWorker, HealthAdmin)
