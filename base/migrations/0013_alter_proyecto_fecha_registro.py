# Generated by Django 4.1.2 on 2022-12-12 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_alter_proyecto_fecha_registro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='Fecha_Registro',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Registro'),
        ),
    ]
