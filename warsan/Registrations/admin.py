from django.contrib import admin
from .models import UserProfile  

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'date_created', 'date_updated')  
admin.site.register(UserProfile, UserProfileAdmin)
