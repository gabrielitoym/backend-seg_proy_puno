# Generated by Django 4.1.2 on 2022-12-12 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_empleado_foto_perfil_alter_empleado_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empleado',
            old_name='Estatus_Employed',
            new_name='Empleado_Activo',
        ),
    ]
