from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


class StateAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name']
admin.site.register(State, StateAdmin)

class DistrictAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name']
admin.site.register(District, DistrictAdmin)

class CityAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name']
admin.site.register(City, CityAdmin)

class AddressAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['city', 'district', 'state']
admin.site.register(Address, AddressAdmin)

class CustomUserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','first_name', 'last_name','email', 'mobile']
    search_fields = ['first_name', 'last_name', 'email', 'mobile']
admin.site.register(CustomUser, CustomUserAdmin)

# Register your models here.
