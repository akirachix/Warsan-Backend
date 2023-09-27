from django.contrib import admin
from .models import Immunization_Record
class ImmunizationAdmin(admin.ModelAdmin):
    list_display= ("child","vaccine","guardian","date_of_administration","next_date_of_administration")
admin.site.register(Immunization_Record,ImmunizationAdmin)   


