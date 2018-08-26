from django.urls import path
from api import views
import datetime
from .apiviews import list_of_trips, list_of_drivers, driver_details, list_of_trips_selected_between_dates, driver_create, LoginView
urlpatterns = [
	path("login/", LoginView.as_view(), name="login"),
	path("api/driver/create/", driver_create.as_view(), name="driver_create"),
	path("api/drivers/", list_of_drivers.as_view(), name="list_of_drivers"),
	path("api/drivers/<int:pk>/", driver_details.as_view(), name ="driver_details"),
	path("api/trips/", list_of_trips.as_view(), name="list_of_trips"),
	path("api/trips/<int:date1>/", list_of_trips_selected_between_dates.as_view(), name="list_of_trips_selected_between_dates"),
]