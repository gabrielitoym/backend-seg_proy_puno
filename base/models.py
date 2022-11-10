from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField()
def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class Empleado(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    DNI = models.CharField(max_length=8, help_text="N° documento")
    Nombres = models.CharField(max_length=30, help_text="Nombre")
    Apellido_Paterno = models.CharField(max_length=150, help_text="Apellido Paterno")
    Apellido_Materno = models.CharField(max_length=150, help_text="Apellido Materno")
    Direccion = models.CharField(max_length=150, help_text="Direccion")
    Telefono = models.CharField(max_length=25, help_text="Telefono")
    Email = models.CharField(max_length=150, help_text="Correo")
    Cargo = models.CharField(max_length=150, help_text="Cargo" ,blank=True, null=True,)
    Oficina = models.CharField(max_length=150, help_text="Oficina" ,null=True,)
    Dependencia = models.CharField(max_length=150, help_text="Dependencia_gerencias")
    Foto_Perfil = models.ImageField(upload_to=upload_to, blank=True, null=True)
    Fecha_Registro = models.DateTimeField(auto_now_add=True)
    Estatus_Employed = models.BooleanField(default=False)