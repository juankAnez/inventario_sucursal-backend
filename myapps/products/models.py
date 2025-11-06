from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = "Categorías"  # Para el admin
    
    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    nombre = models.CharField(max_length=200)
    contacto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    
    class Meta:
        verbose_name_plural = "Proveedores"
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='productos')  # PROTECT mejor que CASCADE
    proveedores = models.ManyToManyField(Proveedor, through='ProductoProveedor', related_name='productos')
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

class ProductoProveedor(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='relaciones_proveedor')
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='relaciones_producto')
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        unique_together = ['producto', 'proveedor']
        verbose_name = "Producto-Proveedor"
        verbose_name_plural = "Productos-Proveedores"


class Garantia(models.Model):
    producto = models.OneToOneField('products.Producto', on_delete=models.CASCADE)
    duracion_meses = models.IntegerField()
    condiciones = models.TextField()
    fecha_inicio = models.DateField(auto_now_add=True)        