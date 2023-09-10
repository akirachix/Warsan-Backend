# child/api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('guardians/', views.guardian_list, name='guardian-list'),
    path('guardians/<int:pk>/', views.guardian_detail, name='guardian-detail'),
    path('children/', views.ChildList.as_view(), name='child-list'),
    path('children/<int:pk>/', views.ChildDetail.as_view(), name='child-detail'),
]
