from django.contrib import admin
from .models import Branch, Warehouse, Location  # ← Esta línea SÍ va en admin.py

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'phone', 'manager']
    search_fields = ['code', 'name', 'manager']
    list_filter = ['manager']

@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['branch', 'code', 'name']
    list_filter = ['branch']
    search_fields = ['code', 'name', 'branch__name']

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['warehouse', 'code']
    list_filter = ['warehouse__branch', 'warehouse']
    search_fields = ['code', 'warehouse__name']