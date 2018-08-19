from django.contrib import admin
from .models import Driver, Manager, Trip
# Register your models here.

admin.site.register(Driver)
admin.site.register(Manager)
admin.site.register(Trip)