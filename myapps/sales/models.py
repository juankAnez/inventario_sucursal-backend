from django.db import models
from django.contrib.auth.models import User

class Batch(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='batches')
    batch_number = models.CharField(max_length=100, unique=True)
    expiration_date = models.DateField(null=True, blank=True)
    manufacturing_date = models.DateField()
    initial_quantity = models.IntegerField()
    current_quantity = models.IntegerField()
    
    class Meta:
        verbose_name_plural = "Batches"
    
    def __str__(self):
        return f"Batch {self.batch_number} - {self.product.name}"

class BranchStock(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='stocks')
    branch = models.ForeignKey('branches.Branch', on_delete=models.CASCADE, related_name='stocks')
    location = models.ForeignKey('branches.Location', on_delete=models.CASCADE, related_name='stocks')
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, related_name='stocks')
    quantity = models.IntegerField(default=0)
    minimum_quantity = models.IntegerField(default=0)
    
    class Meta:
        unique_together = ['product', 'branch', 'location', 'batch']
        verbose_name = "Branch Stock"
        verbose_name_plural = "Branch Stocks"
    
    def __str__(self):
        return f"{self.product} - {self.branch}: {self.quantity}"

class InventoryMovement(models.Model):
    MOVEMENT_TYPES = [
        ('IN', 'In'),
        ('OUT', 'Out'),
        ('ADJUSTMENT', 'Adjustment'),
    ]
    
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='movements')
    branch = models.ForeignKey('branches.Branch', on_delete=models.CASCADE, related_name='movements')
    location = models.ForeignKey('branches.Location', on_delete=models.CASCADE, related_name='movements')
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, related_name='movements')
    movement_type = models.CharField(max_length=10, choices=MOVEMENT_TYPES)
    quantity = models.IntegerField()
    reason = models.TextField()
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='inventory_movements')
    movement_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Inventory Movement"
        verbose_name_plural = "Inventory Movements"
        ordering = ['-movement_date']
    
    def __str__(self):
        return f"{self.movement_type} - {self.product} - {self.quantity}"