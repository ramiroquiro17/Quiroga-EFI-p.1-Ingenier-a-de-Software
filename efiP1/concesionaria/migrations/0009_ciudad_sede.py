# Generated by Django 5.1 on 2024-08-09 15:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concesionaria', '0008_remove_sede_ciudad_id_remove_sede_provincia_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('provincia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='concesionaria.provincia')),
            ],
        ),
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gerente', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=20)),
                ('ciudad_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='concesionaria.ciudad')),
                ('provincia_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='concesionaria.provincia')),
            ],
        ),
    ]
