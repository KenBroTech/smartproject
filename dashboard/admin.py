from django.contrib import admin
from . models import Smart_Meter_Data

# Register your models here.
admin.site.site_header = 'Smart Power Meter Admin Dashboard'


class Smart_Meter_DataAdmin(admin.ModelAdmin):
    list_display = ('location', 'region', 'latitude', 'longitude')


admin.site.register(Smart_Meter_Data, Smart_Meter_DataAdmin)
