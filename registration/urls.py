from django.urls import path
from .views import HealthworkerLoginView

urlpatterns = [
    
    path('login/', HealthworkerLoginView.as_view(), name='healthworker_login'),
]
