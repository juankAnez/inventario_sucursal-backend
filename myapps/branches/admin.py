from django.contrib import admin
from .models import Sucursal, Almacen, Ubicacion

@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre', 'telefono', 'responsable']
    search_fields = ['codigo', 'nombre']

@admin.register(Almacen)
class AlmacenAdmin(admin.ModelAdmin):
    list_display = ['sucursal', 'codigo', 'nombre']
    list_filter = ['sucursal']
    search_fields = ['codigo', 'nombre']

@admin.register(Ubicacion)
class UbicacionAdmin(admin.ModelAdmin):
    list_display = ['almacen', 'codigo']
    list_filter = ['almacen__sucursal']
    search_fields = ['codigo']