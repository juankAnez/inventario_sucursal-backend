from django.contrib import admin
from .models import Category, Supplier, Product, ProductSupplier, Warranty

admin.site.register(Category)
admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(ProductSupplier)
admin.site.register(Warranty)