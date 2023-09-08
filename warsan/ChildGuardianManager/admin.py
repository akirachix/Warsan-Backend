from django.contrib import admin
from .models import Guardian, Child

class GuardianAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'location')
    list_filter = ('location',)
    search_fields = ('first_name', 'last_name', 'phone_number')
    unique_field= ('')

class ChildAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'father_full_name', 'date_of_birth', 'gender', 'guardian')
    list_filter = ('gender',)
    search_fields = ('first_name', 'last_name', 'father_full_name')
    unique_field = ('')

admin.site.register(Guardian, GuardianAdmin)
admin.site.register(Child, ChildAdmin)
