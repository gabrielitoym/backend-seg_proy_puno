# Generated by Django 4.1.2 on 2022-12-19 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0030_alter_pia_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pim',
            name='Year',
            field=models.CharField(help_text='Año asignado', max_length=4),
        ),
    ]
