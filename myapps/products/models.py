from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    
    class Meta:
        verbose_name_plural = "Suppliers"
    
    def __str__(self):
        return self.name

class Product(models.Model):
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    suppliers = models.ManyToManyField(Supplier, through='ProductSupplier', related_name='products')
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.code} - {self.name}"

class ProductSupplier(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='supplier_relations')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='product_relations')
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        unique_together = ['product', 'supplier']
        verbose_name = "Product-Supplier"
        verbose_name_plural = "Products-Suppliers"

class Warranty(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    duration_months = models.IntegerField()
    conditions = models.TextField()
    start_date = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Warranties"