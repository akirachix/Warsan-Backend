# immunization_records/urls.py

from django.urls import path
from . import views



urlpatterns = [
    path('immunization-record/<int:record_id>/update/', views.update_immunization_record, name='update_immunization_record'),
    path('immunization-record/<int:record_id>/', views.view_immunization_record, name='view_immunization_record'),
    path('child/<int:child_id>/upload_immunization/', views.upload_immunization, name='upload_immunization'),

]
