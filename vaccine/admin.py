from django.contrib import admin

from .models import Vaccine

class VaccineAdmin(admin.ModelAdmin):
    list_display = ("name", "target_disease", "date_created")
admin.site.register(Vaccine,VaccineAdmin)
