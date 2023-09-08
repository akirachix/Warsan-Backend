from django.urls import path
from . import views

urlpatterns = [
    path('guardian/create/', views.GuardianCreateView.as_view(), name='create_guardian'),
    path('child/create/', views.ChildCreateView.as_view(), name='create_child'),
]
