from .views import guardian_upload_form
from django.urls import path


urlpatterns=[
    path('guardian/upload/',guardian_upload_form,name='guardian_upload_view'),
  
]
