from django.db import models

class Sucursal(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=200)
    direccion = models.TextField()
    telefono = models.CharField(max_length=20)
    responsable = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Sucursales"
    
    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

class Almacen(models.Model):
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name='almacenes')
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    
    class Meta:
        unique_together = ['sucursal', 'codigo']
        verbose_name = "Almacén"
        verbose_name_plural = "Almacenes"
    
    def __str__(self):
        return f"{self.sucursal.codigo} - {self.nombre}"

class Ubicacion(models.Model):
    almacen = models.ForeignKey(Almacen, on_delete=models.CASCADE, related_name='ubicaciones')
    codigo = models.CharField(max_length=20)
    descripcion = models.TextField(blank=True)
    
    class Meta:
        unique_together = ['almacen', 'codigo']
        verbose_name = "Ubicación"
        verbose_name_plural = "Ubicaciones"
    
    def __str__(self):
        return f"{self.almacen} - {self.codigo}"