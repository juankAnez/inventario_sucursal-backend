from django.contrib import admin
from .models import Batch, BranchStock, InventoryMovement

@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ['batch_number', 'product', 'manufacturing_date', 'expiration_date', 'current_quantity']
    list_filter = ['product']
    search_fields = ['batch_number', 'product__name']

@admin.register(BranchStock)
class BranchStockAdmin(admin.ModelAdmin):
    list_display = ['product', 'branch', 'location', 'batch', 'quantity', 'minimum_quantity']
    list_filter = ['branch', 'product']
    search_fields = ['product__name', 'branch__name']

@admin.register(InventoryMovement)
class InventoryMovementAdmin(admin.ModelAdmin):
    list_display = ['product', 'movement_type', 'quantity', 'branch', 'movement_date', 'user']
    list_filter = ['movement_type', 'branch', 'movement_date']
    search_fields = ['product__name', 'reason']
    readonly_fields = ['movement_date']