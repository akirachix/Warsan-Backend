
from django.urls import path
from .views import Immunization_recordView,ImmunizationDetailView

urlpatterns = [

    path('immunization_record/', Immunization_recordView.as_view(), name='immunization_record_list_view'),
    path('immunization_record/<int:pk>/', ImmunizationDetailView.as_view(), name='immunization_record_detail_view'),  

]

