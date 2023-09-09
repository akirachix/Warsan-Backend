from django.urls import path
from .views import GuardianListView, GuardianDetailView
from .views import ChildListView, ChildDetailView

urlpatterns = [
    path('guardian/', GuardianListView.as_view(), name='guardian_list_view'),
    path('guardian/<int:pk>/', GuardianDetailView.as_view(), name='guardian_detail_view'),
    path('child/', ChildListView.as_view(), name='child_list_view'),
    path('child/<int:pk>/', ChildDetailView.as_view(), name='child_detail_view'),
]
