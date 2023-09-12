# healthCare/urls.py

from django.urls import path
from .views import HealthWorkerListView,HealthWorkerDetailView, HealthWorkerFilterView, HealthWorkerSearchView
from .views import register_user, user_login, user_logout, list_users, get_user_list,  edit_user,delete_user





urlpatterns = [
    path('healthworkers/', HealthWorkerListView.as_view(), name='healthworker-list'),
    path('healthworkers/<int:pk>/', HealthWorkerDetailView.as_view(), name='healthworker-detail'),
    path('healthworkers/search/', HealthWorkerSearchView.as_view(), name='healthworker-search'),
    path('healthworkers/filter/', HealthWorkerFilterView.as_view(), name='healthworker-filter'),
    path('api/list-users/', list_users, name='list_users'),

    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('api/list-users/', get_user_list, name='get_user_list'),
    path('edit-user/<int:user_id>/', edit_user, name='edit_user'),
    path('delete-user/<int:user_id>/',delete_user, name='delete_user'),


]
