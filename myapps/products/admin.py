from django.contrib import admin
from .models import Category, Supplier, Product, ProductSupplier, Warranty

# admin.site.register(Category)
# admin.site.register(Supplier)
# admin.site.register(Product)
# admin.site.register(ProductSupplier)
# admin.site.register(Warranty)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    lista_pantalla = ['name', 'description']
    buscar_campos = ['name']

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    lista_pantalla = ['name', 'contact', 'phone', 'email'] 
    buscar_campos = ['name', 'correo email']

@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'category', 'purchase_price', 'sale_price', 'is_active']
    list_filter = ['category', 'is_active']
    search_fields = ['code', 'name']

@admin.register(ProductSupplier)
class ProductSuppliersAdmin(admin.ModelAdmin):
    list_display = ['product', 'supplier', 'purchase_price']
    list_filter = ['supplier']

@admin.register(Warranty)
class WarrantyAdmin(admin.ModelAdmin):
    list_display = ['product', 'duration_months', 'start_date']
    search_fields = ['product__name']