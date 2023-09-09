from django.urls import path
from .views import LocationListView,StateListView,RegionListView
# ,SpecificRegionListView,SpecificDistrictListView,LocationDetailView,LocationListView

urlpatterns = [
    path("location/",LocationListView.as_view(), name="lovation_list_view"),
    path("regions/",RegionListView.as_view(), name="region_list_view"),

    # path("districts/<str:state_name>/<str:region_name>/",DistrictListView.as_view(), name="district_list_view"),
]
