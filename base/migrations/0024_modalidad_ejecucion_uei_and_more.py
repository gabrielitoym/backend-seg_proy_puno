# Generated by Django 4.1.2 on 2022-12-15 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0023_proyecto_ubicacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modalidad_Ejecucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Modalidad de Ejecucion', max_length=80)),
            ],
            options={
                'verbose_name': 'Modalidad de Ejecucion',
                'verbose_name_plural': 'Modalidades de Ejecucion',
                'db_table': 'Modalidad_Ejecucion',
            },
        ),
        migrations.CreateModel(
            name='UEI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(help_text='Unidad Ejecutora', max_length=80)),
            ],
            options={
                'verbose_name': 'Unidad Ejecutora',
                'verbose_name_plural': 'Unidades Ejecutoras',
                'db_table': 'UEI',
            },
        ),
        migrations.AlterModelOptions(
            name='estado_inversion',
            options={'verbose_name': 'Estado Situacional', 'verbose_name_plural': 'Estados Situacionales'},
        ),
        migrations.AddField(
            model_name='proyecto',
            name='Uei',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.uei'),
        ),
    ]
