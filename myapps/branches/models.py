from django.db import models

class Branch(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=200)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    manager = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Branches"
    
    def __str__(self):
        return f"{self.code} - {self.name}"

class Warehouse(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='warehouses')
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    class Meta:
        unique_together = ['branch', 'code']
        verbose_name = "Warehouse"
        verbose_name_plural = "Warehouses"
    
    def __str__(self):
        return f"{self.branch.code} - {self.name}"

class Location(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='locations')
    code = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    
    class Meta:
        unique_together = ['warehouse', 'code']
        verbose_name = "Location"
        verbose_name_plural = "Locations"
    
    def __str__(self):
        return f"{self.warehouse} - {self.code}"