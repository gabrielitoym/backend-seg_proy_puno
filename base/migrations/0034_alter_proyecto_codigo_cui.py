# Generated by Django 4.1.2 on 2022-12-28 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0033_uei_opmi_uei_unidad_ejecutora_de_inversiones_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='Codigo_CUI',
            field=models.CharField(help_text='Codigo CUI', max_length=7, unique=True),
        ),
    ]
