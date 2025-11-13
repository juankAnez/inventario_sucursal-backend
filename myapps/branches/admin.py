from django.contrib import admin
from .models import Branch, Warehouse, Location

admin.site.register(Branch)
admin.site.register(Warehouse)
admin.site.register(Location)