from django.contrib import admin
from .models import Batch, BranchStock, InventoryMovement

admin.site.register(Batch)
admin.site.register(BranchStock)
admin.site.register(InventoryMovement)