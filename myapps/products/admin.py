from django.contrib import admin
from .models import Categoria, Proveedor, Producto, ProductoProveedor, Garantia

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion']
    search_fields = ['nombre']

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'contacto', 'telefono', 'email']
    search_fields = ['nombre', 'email']

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre', 'categoria', 'precio_compra', 'precio_venta', 'activo']
    list_filter = ['categoria', 'activo']
    search_fields = ['codigo', 'nombre']

@admin.register(ProductoProveedor)
class ProductoProveedorAdmin(admin.ModelAdmin):
    list_display = ['producto', 'proveedor', 'precio_compra']
    list_filter = ['proveedor']

@admin.register(Garantia)
class GarantiaAdmin(admin.ModelAdmin):
    list_display = ['producto', 'duracion_meses', 'fecha_inicio']
    search_fields = ['producto__nombre']