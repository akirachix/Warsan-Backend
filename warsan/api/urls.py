from django.urls import path
from .views import LocationListView,StateListView,RegionListView,SpecificRegionListView,SpecificDistrictListView,LocationDetailView,LocationListView

urlpatterns = [
    path("location/",LocationListView.as_view(), name="location_list_view"),
     path("location/<int:id>",LocationDetailView.as_view(), name="location_detail_view"),
    path("regions/",RegionListView.as_view(), name="region_list_view"),
    path("states/",StateListView.as_view(), name="state_list_view"),

]
