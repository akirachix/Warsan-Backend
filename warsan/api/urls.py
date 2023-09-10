from django.urls import path
from .views import VaccineListView, VaccineDetailView

urlpatterns=[
    path('vaccine/',VaccineListView.as_view(),name='vaccine_list_view'),
    path('vaccine/<int:pk>/',VaccineDetailView.as_view(),name='vaccine_detail_view')
]