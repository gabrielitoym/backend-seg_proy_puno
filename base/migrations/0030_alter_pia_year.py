# Generated by Django 4.1.2 on 2022-12-19 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0029_pim'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pia',
            name='Year',
            field=models.CharField(help_text='Año asignado', max_length=4),
        ),
    ]
