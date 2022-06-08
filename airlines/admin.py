from django.contrib import admin

# from import_export.admin import ImportExportModelAdmin
from .models import Airline

admin.site.register(Airline)
# Register your models here.
# @admin.register(Airline)
# class AirlineAdmin(ImportExportModelAdmin):
#     pass
