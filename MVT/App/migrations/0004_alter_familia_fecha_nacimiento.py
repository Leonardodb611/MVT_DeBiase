# Generated by Django 4.0.3 on 2022-03-30 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_alter_familia_apellido_alter_familia_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familia',
            name='fecha_nacimiento',
            field=models.DateField(auto_now=True),
        ),
    ]
