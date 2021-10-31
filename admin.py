from django.contrib import admin
from vehicle.models import veh

# Register your models here.
class vehAdmin(admin.ModelAdmin):
    list = [ 'speed', 'avgSpeed', 'temperature', 'fuelLevel', 'EngineStatus', 'cam1', 'cam2' ]

admin.site.register(veh, vehAdmin)