# Generated by Django 4.1.2 on 2022-12-14 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0022_ciudad'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='ubicacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.ciudad'),
        ),
    ]
