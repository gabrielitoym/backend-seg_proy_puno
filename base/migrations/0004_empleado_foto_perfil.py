# Generated by Django 4.1.2 on 2022-11-10 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_empleado_cargo_alter_empleado_oficina'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='Foto_Perfil',
            field=models.ImageField(blank=True, null=True, upload_to='employed_perfil/'),
        ),
    ]
