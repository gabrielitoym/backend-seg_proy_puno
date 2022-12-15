# Generated by Django 4.1.2 on 2022-12-14 15:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0018_estado_inversion_alter_proyecto_sector_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='estado_inversion',
            options={'verbose_name': 'Estado de Inversión', 'verbose_name_plural': 'Estado de Inversiones'},
        ),
        migrations.AlterField(
            model_name='empleado',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='estado_inversion',
            name='Estado_Actual',
            field=models.CharField(help_text='Estado Actual', max_length=100),
        ),
        migrations.AlterModelTable(
            name='estado_inversion',
            table='Estado_inversion',
        ),
    ]