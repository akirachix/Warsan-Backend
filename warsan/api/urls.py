from django.urls import path
from .views import VaccineListView

urlpatterns=[
    path('vaccine/',VaccineListView.as_view(),name='vaccine_list_view'),
]