
from .views import immunization_upload_form,immunization_list
from django.urls import path


urlpatterns=[
    path('/immunization/upload',immunization_upload_form,name='immunization_upload_view'),
    path('/immunization/list',immunization_list,name='immunization_list_view'),
]