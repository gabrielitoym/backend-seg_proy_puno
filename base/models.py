from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField()

def upload_to_employed_perfil(instance, filename):
    return 'employed/{filename}'.format(filename=filename)

def upload_to_proyecto_perfil(instance, filename):
    return 'proyecto/{filename}'.format(filename=filename)

class Empleado(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    DNI = models.CharField(max_length=8, help_text="N° documento")
    Nombres = models.CharField(max_length=30, help_text="Nombre")
    Apellido_Paterno = models.CharField(max_length=150, help_text="Apellido Paterno")
    Apellido_Materno = models.CharField(max_length=150, help_text="Apellido Materno")
    Direccion = models.CharField(max_length=150, help_text="Direccion")
    Telefono = models.CharField(max_length=25, help_text="Telefono")
    Email = models.EmailField(help_text="Correo")
    Cargo = models.CharField(max_length=150, help_text="Cargo" ,blank=True, null=True,)
    Oficina = models.CharField(max_length=150, help_text="Oficina" ,null=True,)
    Dependencia = models.CharField(max_length=150, help_text="Dependencia_gerencias")
    Foto_Perfil = models.ImageField(upload_to=upload_to_employed_perfil, blank=True, null=True)
    Fecha_Registro = models.DateTimeField(auto_now_add=True)
    Empleado_Activo = models.BooleanField(default=False)
    def __str__(self):
            return self.Nombres
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'Empleado'

class Sector(models.Model):
    Denominacion = models.CharField(max_length=100, help_text="Denominación")
    def __str__(self):
        return self.Denominacion
    class Meta:
        verbose_name = 'Sector'
        verbose_name_plural = 'Sectores'
        db_table = 'sector'

class Tipo(models.Model):
    name = models.CharField(max_length=100, help_text="name")
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE,null = True,blank=True)
    def __str__(self): 
        return self.name
    class Meta:
        verbose_name = 'Tipo de Inversion'
        verbose_name_plural = 'tipos de Inversion'
        db_table = 'Tipo'

class Estado_Inversion(models.Model):    
    Estado_Actual = models.CharField(max_length=100, help_text="Estado Actual")
    def __str__(self):
        return self.Estado_Actual
    class Meta:
        verbose_name = 'Estado Situacional'
        verbose_name_plural = 'Estados Situacionales'
        db_table = 'Estado_inversion'

class ciudad(models.Model):    
    ubigeo = models.CharField(max_length=6, help_text="ubigeo", blank=False, null=False)
    distrito = models.CharField(max_length=50, help_text="Distrito",blank=True,null=True)
    provincia = models.CharField(max_length=50, help_text="Provincia",blank=True,null=True)
    departamento = models.CharField(max_length=50, help_text="DEpartamento",blank=True,null=True)
    def __str__(self):
        return self.distrito
    class Meta:
        verbose_name = 'Distrito'
        verbose_name_plural = 'Distritos'
        db_table = 'ciudad'

class UEI(models.Model):    
    Nombre = models.CharField(max_length=80, help_text="Unidad Ejecutora", blank=False, null=False)
    def __str__(self):
        return self.Nombre
    class Meta:
        verbose_name = 'Unidad Ejecutora'
        verbose_name_plural = 'Unidades Ejecutoras'
        db_table = 'UEI'

class Modalidad_Ejecucion(models.Model):    
    name = models.CharField(max_length=80, help_text="Modalidad de Ejecucion", blank=False, null=False)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Modalidad de Ejecucion'
        verbose_name_plural = 'Modalidades de Ejecucion'
        db_table = 'Modalidad_Ejecucion'  

class Proyecto(models.Model):
    Codigo_CUI = models.CharField(max_length=7, help_text="Codigo CUI", blank=False, null=False)
    Codigo_SNIP = models.CharField(max_length=6, help_text="Codigo SNIP",blank=True,null=True)
    Nombre = models.TextField( help_text="Nombre Proyecto", null=False)
    Foto_Perfil = models.ImageField(upload_to=upload_to_proyecto_perfil, blank=True, null=True)
    #Tipo = fk
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE,null = True,blank=True)
    #Estado = fk
    estado_inversion = models.ForeignKey(Estado_Inversion, on_delete=models.CASCADE,null = True,blank=True)
    #Modalidad_Ejecucion = fk
    Modalidad_Ejecucion = models.ForeignKey(Modalidad_Ejecucion, on_delete=models.CASCADE,null = True,blank=True)
    #Ubicacion_Ubigeo =fk 
    Uei = models.ForeignKey(UEI, on_delete=models.CASCADE,null = True,blank=True)
    #Duracion = models.DateTimeField(auto_now=True)
    Fecha_Registro = models.DateField(verbose_name="Fecha de Registro",blank=True,null=True)
    Fecha_Inicio = models.DateField(verbose_name="Fecha de Inicio",blank=True,null=True)
    Fecha_Fin = models.DateField(verbose_name="Fecha Fin",blank=True,null=True)
    #id_Unidad_Ejecutora = fk
    #OPMI = fk
    def __str__(self):
        return self.Codigo_CUI
    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        db_table = 'Proyecto'

class Beneficiario(models.Model):    
    ubicacion = models.ForeignKey(ciudad, on_delete=models.CASCADE,null = False,blank=False)
    Proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE,null = False,blank=False)
    Descripcion = models.TextField( help_text="Nombre Proyecto",null = True,blank=True)
    cantidad = models.IntegerField(help_text="Cantidad", null = True,blank=True)
    def __str__(self):
        return self.Descripcion
    class Meta:
        verbose_name = 'Modalidad de Ejecucion'
        verbose_name_plural = 'Modalidades de Ejecucion'
        db_table = 'Beneficiario' 

class Componente(models.Model):  
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE,null = False,blank=False)  
    Nombre = models.TextField(help_text="Componente de Inversion", blank=False, null=False)
    Descripcion  = models.TextField(help_text="Descripcion del componente", blank=True, null=True)
    Costo_Total = models.DecimalField(help_text="Costo total Actualizado",max_digits=9, decimal_places=2)
    Dev_Acumulado = models.DecimalField(help_text="Devengado Acumulado",max_digits=9, decimal_places=2)
    Avance_porcentaje = models.DecimalField(help_text="Porcentaje de avance",max_digits=3, decimal_places=2)
    Fecha_Actualizado = models.DateTimeField(help_text="Fecha de ultima actualizacion",auto_now=False, auto_now_add=False, default=datetime.now)
    Comentario = models.TextField(help_text="Comentario sobre el componente", blank=False, null=False)
    def __str__(self):
        return self.Nombre
    class Meta:
        verbose_name = 'Componente'
        verbose_name_plural = 'Componentes'
        db_table = 'Componente'   

class Situacion_inversion(models.Model):  
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE,null = False,blank=False)
    Descripcion  = models.TextField(help_text="Descripcion del componente", blank=True, null=True)
    Fecha_Modificado = models.DateTimeField(help_text="Fecha de ultima actualizacion", default=datetime.now)
    
    def __str__(self):
        return self.proyecto.Nombre
    class Meta:
        verbose_name = 'Situacion de Inversion'
        verbose_name_plural = 'Situaciones de Inversion'
        db_table = 'Situacion_inversion' 
