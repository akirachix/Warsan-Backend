from django.contrib import admin
from .models import Vaccine

class VaccineAdmin(admin.ModelAdmin):
    list_display = ['vaccine_choice', 'get_target_disease', 'get_recommended_age']

    def get_target_disease(self, obj):
        vaccine_choice = obj.get_vaccine_choice_display()
        if vaccine_choice is not None:
            return vaccine_choice.split(' - ')[1]
        return ''

    def get_recommended_age(self, obj):
        return obj.get_recommended_age()

    get_target_disease.short_description = 'Target Disease'
    get_recommended_age.short_description = 'Recommended Age'

admin.site.register(Vaccine, VaccineAdmin)