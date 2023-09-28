
from django.contrib import admin
from .models import Immunization_Record

class Immunization_RecordAdmin(admin.ModelAdmin):
    list_display = ('child', 'guardian','get_vaccine_display', 'date_of_administration', 'next_date_of_administration', 'status')
    list_filter = ('status', 'vaccine',)
    search_fields = ('child__first_name', 'child__last_name', 'vaccine__vaccine_choice',)

    def get_vaccine_display(self, obj):
        return ', '.join([vaccine.vaccine_choice for vaccine in obj.vaccine.all()])

    get_vaccine_display.short_description = 'Vaccines'

admin.site.register(Immunization_Record, Immunization_RecordAdmin)
