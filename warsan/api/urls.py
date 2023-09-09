from django.urls import path
from .views import GuardianListView, GuardianDetailView
from .views import ChildListView, ChildDetailView


ChildProcessError

urlpatterns = [

    path('guardian/',GuardianListView.as_view(),name='guardian_list_view'),
    path('guardian/',GuardianDetailView.as_view(),name='guardian_detail_view')
    path('guardian/',ChildDetailView.as_view(),name='guardian_list_view'),
    path('guardian/',ChildDetailView.as_view(),name='guardian_detail_view'),
    

    
]
