# Generated by Django 4.1.2 on 2022-12-12 06:03

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_proyecto_codigo_snip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='Foto_Perfil',
            field=models.ImageField(upload_to=base.models.upload_to),
        ),
    ]