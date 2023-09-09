from django.urls import path
from .views import Immunization_recordView

urlpatterns = [
    path('immunization_record/', Immunization_recordView.as_view(), name='immunization_record_list_view'),
    path('immunization_record/<int:pk>/', Immunization_recordView.as_view(), name='immunization_record_detail_view'),
]
# from django.urls import path

# from .views import Immunization_recordView


# urlpatterns = [
#     path('immunization_record/', Immunization_recordView.as_view(), name = 'immunization_record_list_view'),
#     path('immunization_record/<int:id>/', Immunization_recordView.as_view()),

# ]