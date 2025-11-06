from django.db import models
from django.contrib.auth.models import User

class Lote(models.Model):
    producto = models.ForeignKey('products.Producto', on_delete=models.CASCADE, related_name='lotes')
    numero_lote = models.CharField(max_length=100, unique=True)  # Debería ser único
    fecha_vencimiento = models.DateField(null=True, blank=True)
    fecha_fabricacion = models.DateField()
    cantidad_inicial = models.IntegerField()
    cantidad_actual = models.IntegerField()
    
    class Meta:
        verbose_name_plural = "Lotes"
    
    def __str__(self):
        return f"Lote {self.numero_lote} - {self.producto.nombre}"

class StockSucursal(models.Model):
    producto = models.ForeignKey('products.Producto', on_delete=models.CASCADE, related_name='stocks')
    sucursal = models.ForeignKey('branches.Sucursal', on_delete=models.CASCADE, related_name='stocks')
    ubicacion = models.ForeignKey('branches.Ubicacion', on_delete=models.CASCADE, related_name='stocks')
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE, related_name='stocks')
    cantidad = models.IntegerField(default=0)
    cantidad_minima = models.IntegerField(default=0)
    
    class Meta:
        unique_together = ['producto', 'sucursal', 'ubicacion', 'lote']
        verbose_name = "Stock por Sucursal"
        verbose_name_plural = "Stocks por Sucursal"
    
    def __str__(self):
        return f"{self.producto} - {self.sucursal}: {self.cantidad}"

class MovimientoInventario(models.Model):
    TIPO_MOVIMIENTO = [
        ('ENTRADA', 'Entrada'),
        ('SALIDA', 'Salida'),
        ('AJUSTE', 'Ajuste'),
    ]
    
    producto = models.ForeignKey('products.Producto', on_delete=models.CASCADE, related_name='movimientos')
    sucursal = models.ForeignKey('branches.Sucursal', on_delete=models.CASCADE, related_name='movimientos')
    ubicacion = models.ForeignKey('branches.Ubicacion', on_delete=models.CASCADE, related_name='movimientos')
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE, related_name='movimientos')
    tipo_movimiento = models.CharField(max_length=10, choices=TIPO_MOVIMIENTO)
    cantidad = models.IntegerField()
    motivo = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name='movimientos_inventario')  # PROTECT es mejor aquí
    fecha_movimiento = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Movimiento de Inventario"
        verbose_name_plural = "Movimientos de Inventario"
        ordering = ['-fecha_movimiento']  # Más recientes primero
    
    def __str__(self):
        return f"{self.tipo_movimiento} - {self.producto} - {self.cantidad}"