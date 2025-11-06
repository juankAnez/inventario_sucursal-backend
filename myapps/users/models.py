from django.db import models
from django.contrib.auth.models import User

# Perfil extendido para usuarios (opcional)
class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    sucursal = models.ForeignKey('branches.Sucursal', on_delete=models.CASCADE, null=True, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return f"Perfil de {self.usuario.username}"

