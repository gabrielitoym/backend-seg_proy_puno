# Generated by Django 4.1.2 on 2022-12-15 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0024_modalidad_ejecucion_uei_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='Modalidad_Ejecucion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.modalidad_ejecucion'),
        ),
    ]