# Generated by Django 4.1.2 on 2022-11-08 15:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DNI', models.CharField(help_text='N° documento', max_length=8)),
                ('Nombres', models.CharField(help_text='Nombre', max_length=30)),
                ('Apellido_Paterno', models.CharField(help_text='Apellido Paterno', max_length=150)),
                ('Apellido_Materno', models.CharField(help_text='Apellido Materno', max_length=150)),
                ('Direccion', models.CharField(help_text='Direccion', max_length=150)),
                ('Telefono', models.CharField(help_text='Telefono', max_length=25)),
                ('Email', models.CharField(help_text='Correo', max_length=150)),
                ('Cargo', models.CharField(help_text='Cargo', max_length=150)),
                ('Oficina', models.CharField(help_text='Oficina', max_length=150)),
                ('Dependencia', models.CharField(help_text='Dependencia_gerencias', max_length=150)),
                ('Fecha_Registro', models.DateTimeField(auto_now_add=True)),
                ('Estatus_Employed', models.BooleanField(default=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]