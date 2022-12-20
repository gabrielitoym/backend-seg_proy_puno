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
        return self.Nombre
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
        verbose_name = 'beneficiario'
        verbose_name_plural = 'beneficiarios'
        db_table = 'Beneficiario' 

class Componente(models.Model):  
    #Proyecto fk 
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE,null = False,blank=False)  
    Nombre = models.TextField(help_text="Componente de Inversion", blank=False, null=False)
    Componente_Fisico = models.BooleanField(default=False)
    #Descripcion  = models.TextField(help_text="Descripcion del componente", blank=True, null=True)
    #Costo_Total = models.DecimalField(help_text="Costo total Actualizado",max_digits=11, decimal_places=2)
    #Devengado_Acumulado = models.DecimalField(help_text="Devengado Acumulado",max_digits=11, decimal_places=2)
    #Avance_porcentaje = models.DecimalField(help_text="Porcentaje de avance",max_digits=5, decimal_places=2)
    #Fecha_Actualizado = models.DateTimeField(help_text="Fecha de ultima actualizacion",auto_now=False, auto_now_add=False, default=datetime.now)
    #Comentario = models.TextField(help_text="Comentario sobre el componente", blank=False, null=False)
    def __str__(self):
        return self.proyecto.Codigo_CUI+" "+self.Nombre
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

class PIA(models.Model):  
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE,null = False,blank=False)
    Monto_programado = models.DecimalField(help_text="Monto_asignado",max_digits=11, decimal_places=2)
    Year = models.CharField(max_length=4, help_text="Año asignado", blank=False, null=False)
    Monto_programado_01=models.DecimalField(help_text="Monto_asignado_enero",max_digits=11, decimal_places=2)
    Monto_programado_02=models.DecimalField(help_text="Monto_asignado_febrero",max_digits=11, decimal_places=2)
    Monto_programado_03=models.DecimalField(help_text="Monto_asignado_marzo",max_digits=11, decimal_places=2)
    Monto_programado_04=models.DecimalField(help_text="Monto_asignado_abril",max_digits=11, decimal_places=2)
    Monto_programado_05=models.DecimalField(help_text="Monto_asignado_mayo",max_digits=11, decimal_places=2)
    Monto_programado_06=models.DecimalField(help_text="Monto_asignado_junio",max_digits=11, decimal_places=2)
    Monto_programado_07=models.DecimalField(help_text="Monto_asignado_julio",max_digits=11, decimal_places=2)
    Monto_programado_08=models.DecimalField(help_text="Monto_asignado_agosto",max_digits=11, decimal_places=2)
    Monto_programado_09=models.DecimalField(help_text="Monto_asignado_setiembre",max_digits=11, decimal_places=2)
    Monto_programado_10=models.DecimalField(help_text="Monto_asignado_octubre",max_digits=11, decimal_places=2)
    Monto_programado_11=models.DecimalField(help_text="Monto_asignado_noviembre",max_digits=11, decimal_places=2)
    Monto_programado_12=models.DecimalField(help_text="Monto_asignado_diciembre",max_digits=11, decimal_places=2)
    
    def __str__(self):
        return self.proyecto.Nombre + " "+self.Year
    class Meta:
        verbose_name = 'PIA'
        verbose_name_plural = 'PIAs'
        db_table = 'PIA'  

class PIM(models.Model):  
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE,null = False,blank=False)
    Monto_actualizado = models.DecimalField(help_text="Monto_actualizado",max_digits=11, decimal_places=2)
    Year = models.CharField(max_length=4, help_text="Año asignado", blank=False, null=False)
    Monto_actualizado_01=models.DecimalField(help_text="Monto_actualizado_enero",max_digits=11, decimal_places=2)
    Monto_actualizado_02=models.DecimalField(help_text="Monto_actualizado_febrero",max_digits=11, decimal_places=2)
    Monto_actualizado_03=models.DecimalField(help_text="Monto_actualizado_marzo",max_digits=11, decimal_places=2)
    Monto_actualizado_04=models.DecimalField(help_text="Monto_actualizado_abril",max_digits=11, decimal_places=2)
    Monto_actualizado_05=models.DecimalField(help_text="Monto_actualizado_mayo",max_digits=11, decimal_places=2)
    Monto_actualizado_06=models.DecimalField(help_text="Monto_actualizado_junio",max_digits=11, decimal_places=2)
    Monto_actualizado_07=models.DecimalField(help_text="Monto_actualizado_julio",max_digits=11, decimal_places=2)
    Monto_actualizado_08=models.DecimalField(help_text="Monto_actualizado_agosto",max_digits=11, decimal_places=2)
    Monto_actualizado_09=models.DecimalField(help_text="Monto_actualizado_setiembre",max_digits=11, decimal_places=2)
    Monto_actualizado_10=models.DecimalField(help_text="Monto_actualizado_octubre",max_digits=11, decimal_places=2)
    Monto_actualizado_11=models.DecimalField(help_text="Monto_actualizado_noviembre",max_digits=11, decimal_places=2)
    Monto_actualizado_12=models.DecimalField(help_text="Monto_actualizado_diciembre",max_digits=11, decimal_places=2)
    
    def __str__(self):
        return self.proyecto.Nombre + " "+self.Year
    class Meta:
        verbose_name = 'PIM'
        verbose_name_plural = 'PIMs'
        db_table = 'PIM'  

class Devengado(models.Model):  
    PIM = models.ForeignKey(PIM, on_delete=models.CASCADE,null = False,blank=False)
    dev_Anual = models.DecimalField(help_text="Monto_actualizado",max_digits=11, decimal_places=2)
    Year = models.CharField(max_length=4, help_text="Año asignado", blank=False, null=False)
    Monto_devengado_01=models.DecimalField(help_text="Monto_devengado_enero",max_digits=11, decimal_places=2)
    Monto_devengado_02=models.DecimalField(help_text="Monto_devengado_febrero",max_digits=11, decimal_places=2)
    Monto_devengado_03=models.DecimalField(help_text="Monto_devengado_marzo",max_digits=11, decimal_places=2)
    Monto_devengado_04=models.DecimalField(help_text="Monto_devengado_abril",max_digits=11, decimal_places=2)
    Monto_devengado_05=models.DecimalField(help_text="Monto_devengado_mayo",max_digits=11, decimal_places=2)
    Monto_devengado_06=models.DecimalField(help_text="Monto_devengado_junio",max_digits=11, decimal_places=2)
    Monto_devengado_07=models.DecimalField(help_text="Monto_devengado_julio",max_digits=11, decimal_places=2)
    Monto_devengado_08=models.DecimalField(help_text="Monto_devengado_agosto",max_digits=11, decimal_places=2)
    Monto_devengado_09=models.DecimalField(help_text="Monto_devengado_setiembre",max_digits=11, decimal_places=2)
    Monto_devengado_10=models.DecimalField(help_text="Monto_devengado_octubre",max_digits=11, decimal_places=2)
    Monto_devengado_11=models.DecimalField(help_text="Monto_devengado_noviembre",max_digits=11, decimal_places=2)
    Monto_devengado_12=models.DecimalField(help_text="Monto_devengado_diciembre",max_digits=11, decimal_places=2)
    
    def __str__(self):
        return self.proyecto.Nombre + " "+self.Year
    class Meta:
        verbose_name = 'Devengado'
        verbose_name_plural = 'Devengados'
        db_table = 'devengado'  

class Certificacion(models.Model):  
    PIM = models.ForeignKey(PIM, on_delete=models.CASCADE,null = False,blank=False)
    cert_Anual = models.DecimalField(help_text="Monto_actualizado",max_digits=11, decimal_places=2)
    Year = models.CharField(max_length=4, help_text="Año asignado", blank=False, null=False)
    Monto_certificado_01=models.DecimalField(help_text="Monto_certificado_enero",max_digits=11, decimal_places=2)
    Monto_certificado_02=models.DecimalField(help_text="Monto_certificado_febrero",max_digits=11, decimal_places=2)
    Monto_certificado_03=models.DecimalField(help_text="Monto_certificado_marzo",max_digits=11, decimal_places=2)
    Monto_certificado_04=models.DecimalField(help_text="Monto_certificado_abril",max_digits=11, decimal_places=2)
    Monto_certificado_05=models.DecimalField(help_text="Monto_certificado_mayo",max_digits=11, decimal_places=2)
    Monto_certificado_06=models.DecimalField(help_text="Monto_certificado_junio",max_digits=11, decimal_places=2)
    Monto_certificado_07=models.DecimalField(help_text="Monto_certificado_julio",max_digits=11, decimal_places=2)
    Monto_certificado_08=models.DecimalField(help_text="Monto_certificado_agosto",max_digits=11, decimal_places=2)
    Monto_certificado_09=models.DecimalField(help_text="Monto_certificado_setiembre",max_digits=11, decimal_places=2)
    Monto_certificado_10=models.DecimalField(help_text="Monto_certificado_octubre",max_digits=11, decimal_places=2)
    Monto_certificado_11=models.DecimalField(help_text="Monto_certificado_noviembre",max_digits=11, decimal_places=2)
    Monto_certificado_12=models.DecimalField(help_text="Monto_certificado_diciembre",max_digits=11, decimal_places=2)
    
    def __str__(self):
        return self.proyecto.Nombre + " "+self.Year
    class Meta:
        verbose_name = 'Certificación'
        verbose_name_plural = 'Certificaciones'
        db_table = 'certificacion'  

class Costo_general(models.Model):  
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE,null = False,blank=False)
    Costo_total = models.DecimalField(help_text="Monto_actualizado",max_digits=11, decimal_places=2)
    Devengado_acumulado = models.DecimalField(help_text="Devengado_acumulado",max_digits=11, decimal_places=2)
    certificacion_Acumulada = models.DecimalField(help_text="certificacion_acumulada",max_digits=11, decimal_places=2)
    Last_Year = models.CharField(max_length=4, help_text="Ultimo Año actualizado", blank=False, null=False)

    def __str__(self):
        return self.proyecto.Nombre
    class Meta:
        verbose_name = 'Costo general'
        verbose_name_plural = 'Costos generales'
        db_table = 'costo_general'  
