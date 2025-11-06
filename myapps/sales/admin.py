from django.contrib import admin
from .models import Lote, StockSucursal, MovimientoInventario

@admin.register(Lote)
class LoteAdmin(admin.ModelAdmin):
    list_display = ['numero_lote', 'producto', 'fecha_fabricacion', 'fecha_vencimiento', 'cantidad_actual']
    list_filter = ['producto']
    search_fields = ['numero_lote', 'producto__nombre']

@admin.register(StockSucursal)
class StockSucursalAdmin(admin.ModelAdmin):
    list_display = ['producto', 'sucursal', 'ubicacion', 'lote', 'cantidad', 'cantidad_minima']
    list_filter = ['sucursal', 'producto']
    search_fields = ['producto__nombre', 'sucursal__nombre']

@admin.register(MovimientoInventario)
class MovimientoInventarioAdmin(admin.ModelAdmin):
    list_display = ['producto', 'tipo_movimiento', 'cantidad', 'sucursal', 'fecha_movimiento', 'usuario']
    list_filter = ['tipo_movimiento', 'sucursal', 'fecha_movimiento']
    search_fields = ['producto__nombre', 'motivo']
    readonly_fields = ['fecha_movimiento']