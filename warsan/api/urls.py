# healthCare/urls.py

from django.urls import path
from .views import HealthWorkerListView,HealthWorkerDetailView, HealthWorkerFilterView, HealthWorkerSearchView

urlpatterns = [
    path('healthworkers/', HealthWorkerListView.as_view(), name='healthworker-list'),
    path('healthworkers/<int:pk>/', HealthWorkerDetailView.as_view(), name='healthworker-detail'),
    path('healthworkers/search/', HealthWorkerSearchView.as_view(), name='healthworker-search'),
    path('healthworkers/filter/', HealthWorkerFilterView.as_view(), name='healthworker-filter'),
]
