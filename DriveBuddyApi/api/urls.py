from django.urls import path
from api import views
from .views import list_of_trips, list_of_drivers

urlpatterns = [
	path('api/drivers/', views.list_of_drivers, name='list_of_drivers'),
	path('api/trips/', views.list_of_trips, name='list_of_trips')
]