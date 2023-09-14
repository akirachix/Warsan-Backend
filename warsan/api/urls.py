

from django.urls import path
from .views import Immunization_recordView,ImmunizationDetailView
from .views import VaccineListView, VaccineDetailView
from .views import LocationListView,StateListView,SpecificRegionListView,SpecificDistrictListView,LocationDetailView,LocationListView





urlpatterns = [
    path('ngo/signup/', views.ngo_signup, name='ngo-signup'),
    path('ngo/logout/', views.ngo_logout, name='ngo-logout'),
    path('customusers/', views.CustomUserList.as_view(), name='customuser-list'),
    path('customusers/<int:pk>/', views.CustomUserDetail.as_view(), name='customuser-detail'),
    path('healthworkers/', views.HealthworkerList.as_view(), name='healthworker-list'),
    path('healthworkers/<int:pk>/', views.healthworker_detail, name='healthworker-detail'),
    path('healthworker/signup/', views.healthworker_signup, name='healthworker-signup'),
    path('healthworker/logout/', views.healthworker_logout, name='healthworker-logout'),
    path('healthworker/login/', views.healthworker_login, name='healthworker-login'),
    path('ngo/login/', views.ngo_login, name='ngo-login'),
    path('vaccine/',VaccineListView.as_view(),name='vaccine_list_view'),
    path('vaccine/<int:pk>/',VaccineDetailView.as_view(),name='vaccine_detail_view')
    path('immunization_record/', Immunization_recordView.as_view(), name='immunization_record_list_view'),
    path('immunization_record/<int:pk>/', ImmunizationDetailView.as_view(), name='immunization_record_detail_view'), 
    path("location/",LocationListView.as_view(), name="location_list_view"),
    path("location/<int:id>",LocationDetailView.as_view(), name="location_detail_view"),
    path("states/",StateListView.as_view(), name="state_list_view"),
]



