from django.contrib import admin
from .models import category, vehicle_entry

# Register your models here.
class categorycustomisation(admin.ModelAdmin):
    list_display = ['parking_area_number']
class vehiclecustomisation(admin.ModelAdmin):
    list_display = ['vehicle_no', 'parking_charge']

admin.site.register(category,categorycustomisation)
admin.site.register(vehicle_entry, vehiclecustomisation)
