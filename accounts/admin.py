from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.admin import UserAdmin
from .forms import *


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
    list_display = ['address', 'city', 'district', 'state']
admin.site.register(Address, AddressAdmin)

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'dob', 'role', 'mobile', 'is_staff', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('dob', 'role', 'mobile')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('dob', 'role', 'mobile')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

# Register your models here.
