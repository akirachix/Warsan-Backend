from django.urls import path
from .views import LocationListView,StateListView,SpecificRegionListView,SpecificDistrictListView,LocationDetailView,LocationListView


urlpatterns = [
    path("location/",LocationListView.as_view(), name="location_list_view"),
     path("location/<int:id>",LocationDetailView.as_view(), name="location_detail_view"),
    path("regions/",SpecificRegionListView.as_view(), name="specific_region_list_view"),
    path("states/",StateListView.as_view(), name="state_list_view"),

]
