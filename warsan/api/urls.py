# healthCare/urls.py

from django.urls import path
from .views import HealthWorkerListView,HealthWorkerDetailView

urlpatterns = [
    path('healthworkers/', HealthWorkerListView.as_view(), name='healthworker-list'),
    path('healthworkers/<int:pk>/', HealthWorkerDetailView.as_view(), name='healthworker-detail'),
]
