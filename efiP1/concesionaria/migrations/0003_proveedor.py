# Generated by Django 5.1 on 2024-08-09 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concesionaria', '0002_color_provincia_ciudad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('direccion', models.TextField()),
                ('telefono', models.CharField(max_length=15)),
            ],
        ),
    ]
