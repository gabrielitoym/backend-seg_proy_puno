# Generated by Django 4.1.2 on 2022-12-12 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_alter_proyecto_foto_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='Codigo_SNIP',
            field=models.CharField(help_text='Codigo SNIP', max_length=6),
        ),
    ]
